#!/usr/bin/env python3
"""
J.A.R.V.I.S. — Git AutoPush система
Автоматическая отправка изменений на GitHub с умными правилами.

by KotMir — когда ты слишком занят хакингом для коммитов вручную.

Использование:
    python git_autopush.py              — включить демон (слушает файловые события)
    python git_autopush.py --once       — один раз запушить текущие изменения
    python git_autopush.py --interval 60 — коммитить каждые 60 секунд
    python git_autopush.py --dry-run    — показать что будет закоммичено
"""

import argparse
import logging
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("JARVIS.GitAutoPush")

# Конфиг
REPO_ROOT = Path(__file__).parent
GIT_IGNORE_FILES = {".env", ".env.example", "*.pyc", "__pycache__", "config/settings.json"}
GIT_IGNORE_DIRS = {"venv", ".venv", "env", "__pycache__", ".git", ".pytest_cache"}


def run_git_command(cmd: str, check: bool = True) -> subprocess.CompletedProcess:
    """Выполнить git-команду с обработкой ошибок."""
    logger.debug(f"$ git {cmd}")
    try:
        result = subprocess.run(
            f"git {cmd}",
            shell=True,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False
        )
        if check and result.returncode != 0:
            logger.error(f"Git ошибка: {result.stderr}")
            return None
        return result
    except Exception as e:
        logger.error(f"Ошибка выполнения git: {e}")
        return None


def get_git_status() -> dict:
    """Получить статус репозитория."""
    result = run_git_command("status --porcelain", check=False)
    if not result:
        return {"modified": [], "untracked": [], "deleted": []}

    modified = []
    untracked = []
    deleted = []

    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        status = line[:2]
        filename = line[3:]

        # Игнорируем .env файлы
        if any(filename.endswith(ignore) for ignore in [".env", "*.pyc"]):
            continue

        if status == "M ":
            modified.append(filename)
        elif status == "??":
            untracked.append(filename)
        elif status == "D ":
            deleted.append(filename)

    return {"modified": modified, "untracked": untracked, "deleted": deleted}


def has_changes() -> bool:
    """Есть ли незафиксированные изменения?"""
    status = get_git_status()
    return bool(status["modified"] or status["untracked"] or status["deleted"])


def get_current_branch() -> str | None:
    """Получить название текущей ветки."""
    result = run_git_command("rev-parse --abbrev-ref HEAD", check=False)
    if result and result.returncode == 0:
        return result.stdout.strip()
    return None


def generate_commit_message(status: dict) -> str:
    """Сгенерировать умное сообщение коммита."""
    timestamp = datetime.now().strftime("%H:%M:%S")

    parts = []
    if status["modified"]:
        count = len(status["modified"])
        parts.append(f"Обновлено {count} файлов")
        if count <= 3:
            parts.append("(" + ", ".join(Path(f).name for f in status["modified"][:3]) + ")")

    if status["untracked"]:
        count = len(status["untracked"])
        parts.append(f"Добавлено {count} новых")

    if status["deleted"]:
        count = len(status["deleted"])
        parts.append(f"Удалено {count}")

    msg = " | ".join(parts) if parts else "Автоматический коммит"
    msg = f"🤖 {msg} [{timestamp}] by KotMir"

    return msg


def stage_all_changes(dry_run: bool = False) -> bool:
    """Добавить все изменения в staging area."""
    if dry_run:
        status = get_git_status()
        logger.info(f"[DRY-RUN] Будут закоммичены:")
        for f in status["modified"]:
            logger.info(f"  M {f}")
        for f in status["untracked"]:
            logger.info(f"  ? {f}")
        for f in status["deleted"]:
            logger.info(f"  D {f}")
        return True

    result = run_git_command("add -A", check=False)
    return result and result.returncode == 0


def commit_changes(message: str, dry_run: bool = False) -> bool:
    """Создать коммит."""
    if dry_run:
        logger.info(f"[DRY-RUN] Коммит сообщение: {message}")
        return True

    # Экранировать спецсимволы в сообщении для shell
    message_escaped = message.replace('"', '\\"')
    result = run_git_command(f'commit -m "{message_escaped}" --no-verify', check=False)

    if result and result.returncode == 0:
        logger.info(f"✓ Коммит: {message}")
        return True
    elif "nothing to commit" in result.stderr:
        logger.info("~ Нечего коммитить")
        return True  # Это не ошибка
    else:
        logger.error(f"Ошибка коммита: {result.stderr}")
        return False


def push_changes(dry_run: bool = False) -> bool:
    """Отправить изменения на удалённый репозиторий."""
    branch = get_current_branch()
    if not branch:
        logger.error("Не удалось определить текущую ветку")
        return False

    if dry_run:
        logger.info(f"[DRY-RUN] Будет отправлено в {branch}")
        return True

    result = run_git_command(f"push origin {branch}", check=False)

    if result and result.returncode == 0:
        logger.info(f"✓ Отправлено в {branch}")
        return True
    elif "everything up-to-date" in result.stderr or "nothing to commit" in result.stderr:
        logger.info(f"~ Уже актуально")
        return True
    else:
        logger.error(f"Ошибка отправки: {result.stderr}")
        return False


def autopush_once(dry_run: bool = False) -> bool:
    """Выполнить одну операцию push: stage → commit → push."""
    logger.info("━━━ AutoPush запущен ━━━")

    if not has_changes():
        logger.info("~ Нет изменений для отправки")
        return True

    status = get_git_status()
    logger.info(f"Найдено: {len(status['modified'])} изменений, "
                f"{len(status['untracked'])} новых, {len(status['deleted'])} удалено")

    if not stage_all_changes(dry_run):
        logger.error("✗ Ошибка при добавлении файлов в staging")
        return False

    message = generate_commit_message(status)
    if not commit_changes(message, dry_run):
        logger.error("✗ Ошибка при создании коммита")
        return False

    if not push_changes(dry_run):
        logger.error("✗ Ошибка при отправке на GitHub")
        return False

    logger.info("✓ AutoPush успешно завершен!\n")
    return True


def autopush_daemon(interval: int = 300):
    """Запустить демон AutoPush (слушает каждые N секунд)."""
    logger.info(f"🤖 Демон AutoPush запущен (проверка каждые {interval}с)")
    logger.info("Нажмите Ctrl+C для выхода\n")

    try:
        while True:
            if has_changes():
                autopush_once(dry_run=False)
            else:
                logger.debug(f"[{datetime.now().strftime('%H:%M:%S')}] Нет изменений, проверка...")

            time.sleep(interval)
    except KeyboardInterrupt:
        logger.info("\n✓ Демон остановлен")


def main():
    parser = argparse.ArgumentParser(
        description="J.A.R.V.I.S. Git AutoPush — автоматическая отправка на GitHub",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Примеры:
  %(prog)s --once               выполнить одну операцию push
  %(prog)s --interval 60        коммитить каждые 60 секунд
  %(prog)s --dry-run            показать что будет закоммичено (без действий)
  %(prog)s --daemon             слушать файловые события (по умолчанию)
"""
    )
    parser.add_argument("--once", action="store_true", help="одна операция push и выход")
    parser.add_argument("--daemon", action="store_true", help="слушать файловые события")
    parser.add_argument("--interval", type=int, default=300, help="интервал проверки (сек, по умолчанию 300)")
    parser.add_argument("--dry-run", action="store_true", help="показать что будет без действий")
    parser.add_argument("-v", "--verbose", action="store_true", help="подробные логи")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Проверить что находимся в git репозитории
    if not (REPO_ROOT / ".git").exists():
        logger.error("✗ Не обнаружен .git репозиторий в текущей папке!")
        sys.exit(1)

    logger.info(f"📁 Репозиторий: {REPO_ROOT}")
    logger.info(f"🌿 Ветка: {get_current_branch()}")

    if args.once:
        success = autopush_once(dry_run=args.dry_run)
        sys.exit(0 if success else 1)
    elif args.dry_run:
        autopush_once(dry_run=True)
        sys.exit(0)
    else:
        autopush_daemon(interval=args.interval)


if __name__ == "__main__":
    main()
