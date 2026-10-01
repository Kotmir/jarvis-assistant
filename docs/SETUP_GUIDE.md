# 📖 Установка JARVIS Lime-Hacker Edition

**by KotMir** — Полный гайд по обновлению

## 📋 Предварительно

- Windows 10+ или Linux/macOS
- Python 3.9+
- Git установлен
- Репозиторий: https://github.com/Kotmir/jarvis-assistant

## ⚡ Быстрая установка (5 минут)

### Шаг 1: Загрузить файлы улучшений

Скопируй эти файлы в корневую папку проекта:
- `style_lime.py` → заменит `jarvis/ui/style.py`
- `git_autopush.py` → в корень (запускать отсюда)
- `autopush.bat` → в корень (для Windows)

### Шаг 2: Установить новую тему

```bash
cd C:\Users\KotMir_You\Desktop\Jarvis-main

# Резервная копия старой темы (на случай если понадобится вернуть)
copy jarvis\ui\style.py jarvis\ui\style_backup.py

# Установить новую тему
copy style_lime.py jarvis\ui\style.py
```

### Шаг 3: Тестировать

```bash
# Запустить JARVIS и проверить новый зелёный вид
python main.py
```

Должны увидеть:
- 🟢 Зелёный неоновый интерфейс
- ⚡ Свечение вокруг кнопок
- 📊 Тёмный фон `#0a0e1a`
- 🔤 Монофонт в логах

### Шаг 4: Настроить AutoPush

```bash
# Проверить текущие изменения (сухой прогон)
python git_autopush.py --dry-run

# Если всё выглядит хорошо, коммитить первый раз
python git_autopush.py --once

# Дальше может работать демон фоном
# python git_autopush.py --daemon
```

## 📚 Полная пошаговая установка

### 1️⃣ Проверка окружения

```bash
# Проверить Python
python --version          # должно быть 3.9 или выше

# Проверить Git
git --version             # должно быть любое

# Проверить что мы в папке проекта
cd C:\Users\KotMir_You\Desktop\Jarvis-main
git status                # должна показать статус репо
```

### 2️⃣ Резервная копия

Всегда делай backup перед серьёзными изменениями:

```bash
# Резервные копии важных файлов
copy jarvis\ui\style.py jarvis\ui\style_backup.py
copy .env .env.backup

# Git может помочь откатить если что-то пошло не так
git status                # проверить что ничего не потеряется
```

### 3️⃣ Установка темы

```bash
# Копируем новую тему (Windows)
copy style_lime.py jarvis\ui\style.py

# Или на Linux/macOS
cp style_lime.py jarvis/ui/style.py

# Проверить что файл скопирован
ls -la jarvis/ui/style.py
```

### 4️⃣ Установка AutoPush

```bash
# Копируем скрипт (Windows)
copy git_autopush.py .
copy autopush.bat .

# Или на Linux/macOS
cp git_autopush.py .
chmod +x git_autopush.py      # разрешить выполнение

# Проверить
python git_autopush.py --help   # должна показать справку
```

### 5️⃣ Конфигурация Git (один раз)

```bash
# Задать имя пользователя (локально для этого репо)
git config user.name "KotMir"
git config user.email "leula2001@outlook.com"

# Или глобально (для всех репо)
git config --global user.name "KotMir"
git config --global user.email "leula2001@outlook.com"

# Проверить
git config user.name          # должна показать "KotMir"
```

### 6️⃣ Тестирование

```bash
# 1. Запустить JARVIS и убедиться что тема работает
python main.py

# После запуска:
#   ✓ Должна быть зелёная тема
#   ✓ Кнопки светятся зелёным
#   ✓ Текст монофонта в логах
#   ✓ Вверху: "J.A.R.V.I.S. ONLINE" зелёный

# 2. Тестировать AutoPush (сухой прогон)
python git_autopush.py --dry-run

# Должна показать:
#   ✓ Текущую ветку
#   ✓ Найденные изменения
#   ✓ Что будет закоммичено
#   ✓ ИМЯ коммита с временем и "by KotMir"
```

### 7️⃣ Первый реальный коммит с новой темой

```bash
# Сейчас в репо есть изменения (новые файлы)
git status                      # проверить

# Коммитить первый раз с новой темой
python git_autopush.py --once

# Проверить что всё отправилось
git log --oneline -3            # должна показать последний коммит с временем

# На GitHub должен появиться новый коммит с:
# 🤖 Обновлено 1 файлов | Добавлено 3 новых [XX:XX:XX] by KotMir
```

## 🚀 Использование AutoPush

### Вариант 1: Ручной коммит (когда захочешь)

```bash
# Один раз коммитить и отправить
python git_autopush.py --once

# Это эквивалентно:
# git add -A
# git commit -m "🤖 Обновлено X файлов | Добавлено Y новых [XX:XX:XX] by KotMir"
# git push origin main
```

### Вариант 2: Демон (фоном)

```bash
# Включить демон (проверяет каждые 300 сек = 5 минут)
python git_autopush.py --daemon

# Или чаще (каждые 60 сек)
python git_autopush.py --daemon --interval 60

# Нажать Ctrl+C чтобы выключить
```

### Вариант 3: Батник для Windows

Создать ярлык на рабочем столе:

```
Цель: C:\Users\KotMir_You\Desktop\Jarvis-main\autopush.bat daemon
Начать в: C:\Users\KotMir_You\Desktop\Jarvis-main
```

Двойной клик = запустить демон в фоне

### Вариант 4: Планировщик Windows

Запускать AutoPush каждые N минут через Планировщик задач:

```powershell
# В PowerShell (как админ):
$TaskName = "JARVIS_AutoPush"
$TaskPath = "C:\Users\KotMir_You\Desktop\Jarvis-main"
$Action = New-ScheduledTaskAction -Execute "python" -Argument "$TaskPath\git_autopush.py --once" -WorkingDirectory $TaskPath
$Trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 5) -AtLogon
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -RunLevel Highest
```

## 🔧 Решение проблем

### Проблема: "Тема не меняется"

```bash
# Убедиться что файл скопирован правильно
ls -la jarvis/ui/style.py

# Перезапустить JARVIS
python main.py

# Если не помогло, вернуть старую тему
copy jarvis\ui\style_backup.py jarvis\ui\style.py
```

### Проблема: AutoPush ошибка при push

```bash
# Проверить статус git
git status

# Проверить что есть connection к GitHub
ping github.com

# Проверить SSH ключи (если используешь SSH)
ssh -T git@github.com

# Или использовать HTTPS вместо SSH
git remote set-url origin https://github.com/Kotmir/jarvis-assistant.git
```

### Проблема: "Git не найден"

```bash
# Установить Git https://git-scm.com/download/win
# После установки перезагрузиться

# Проверить
git --version
```

### Проблема: .env файл хранится в Git

```bash
# Убедиться что .env в .gitignore
type .gitignore | find ".env"

# Если нет, добавить вручную
echo .env >> .gitignore
echo .env.* >> .gitignore

# Удалить .env из кеша Git (если уже там)
git rm --cached .env
git commit -m "🤖 Удалено .env из Git [XX:XX:XX] by KotMir"
```

## ✅ Финальный чекпас

После установки проверить:

- [ ] Тема применена и JARVIS показывает зелёный интерфейс
- [ ] AutoPush скрипт работает (`python git_autopush.py --help`)
- [ ] Git-конфиг настроен (`git config user.name`)
- [ ] Первый коммит отправлен на GitHub
- [ ] `.env` не хранится в Git
- [ ] Демон AutoPush может работать фоном (опционально)

## 📞 Контакты

- 📧 Email: leula2001@outlook.com
- 🐙 GitHub: https://github.com/Kotmir/jarvis-assistant
- 💬 Discord: ищите на серверах программистов

## 🟢 Слоган

```
JARVIS Lime-Hacker Edition by KotMir
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Зелёный свет, умный мозг, автоматический коммит.
```

---

**Версия**: 1.0 Lime-Hacker Edition
**Дата**: Октябрь 2026
**Автор**: KotMir
**Лиц**: MIT (как оригинальный JARVIS)
