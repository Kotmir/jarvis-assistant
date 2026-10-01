# 🟢 J.A.R.V.I.S. Lime Hacker Edition

## 📌 Информация о проекте

### Исходный проект
- **Оригинальный автор**: [RustamovAkrom](https://github.com/RustamovAkrom)
- **Исходный репо**: https://github.com/RustamovAkrom/JARVIS
- **Описание**: J.A.R.V.I.S. — голосовой ассистент для Windows с поддержкой Gemini, OpenAI, Spotify

### Этот форк (Lime Hacker Edition)
- **Форк от**: [KotMir](https://github.com/Kotmir)
- **Репо форка**: https://github.com/Kotmir/jarvis-assistant
- **Улучшения**: 
  - 🟢 Новая лайм-хакерская тема
  - 🤖 Git AutoPush (автоматические коммиты)
  - 📚 Батники для быстрого пуша
  - 📖 Полная документация на русском

---

## 🙏 Благодарности

Спасибо **RustamovAkrom** за отличный проект JARVIS! 
- Архитектура очень крутая
- Интеграция с Gemini Live работает идеально
- Код читабельный и расширяемый

Этот форк просто добавляет красоты (лайм-тему) и удобства (автопуш). 🚀

---

## 📚 Как связаны репо

```
Original (RustamovAkrom)
└── https://github.com/RustamovAkrom/JARVIS
    │
    ├─ Issues, PRs, Development
    │
    └──> Fork by KotMir
         └── https://github.com/Kotmir/jarvis-assistant
             └── Lime Hacker Edition
                 ├── New Theme (style_lime.py)
                 ├── AutoPush Scripts
                 ├── Batch Files
                 └── Russian Documentation
```

---

## 🔄 Синхронизация с оригиналом

Если в оригинальном JARVIS появятся новые фишки, их можно:

1. **Вручную переделать** под лайм-тему
2. **Через git merge** (если не было конфликтов в UI)
3. **Cherry-pick** нужные коммиты

```bash
# Добавить оригинальный репо как remote
git remote add upstream https://github.com/RustamovAkrom/JARVIS

# Получить обновления
git fetch upstream

# Смотреть что новое
git log upstream/main --oneline

# Если хочешь смерджить (осторожно с темой!)
git merge upstream/main
```

---

## 📋 Основные файлы проекта

### 🔧 Оригинальные файлы (от RustamovAkrom)
```
jarvis/
├── brain/          — AI мозг (Gemini, OpenAI, Claude)
├── core/           — основной ассистент
├── services/       — Spotify, VPN, News, YouTube
├── tools/          — команды (Apps, Files, Discord, etc)
├── ui/             — Qt интерфейс
├── voice/          — STT, TTS, Gemini Live
└── utils/          — вспомогательные функции

config/             — конфиги и данные
scripts/            — тестовые скрипты
tests/              — unit тесты
```

### 🟢 Новые файлы (от KotMir)
```
style_lime.py                — новая тема
git_autopush.py              — автопуш скрипт (Python)
autopush_simple.bat          — батник (быстрый)
quick_push.bat               — батник (выбор типа)
update_and_push.bat          — батник (полный контроль)
README_LIME_EDITION.md       — быстрый старт
SETUP_GUIDE.md               — полный гайд
THEME_CHANGES.md             — описание темы
UPDATES.md                   — что изменилось
BATCH_FILES_GUIDE.md         — справка по батникам
```

---

## 🚀 Быстрый старт

### Установка лайм-темы
```bash
copy style_lime.py jarvis\ui\style.py
python main.py
```

### Использование автопуша (Python)
```bash
python git_autopush.py --once
python git_autopush.py --daemon
```

### Использование батников (Windows)
```bash
autopush_simple.bat          # Самый быстрый
quick_push.bat               # Со выбором
update_and_push.bat          # Полный контроль
```

---

## 📜 Лицензия

Этот форк использует ту же лицензию что и оригинальный проект.

- **Оригинальный JARVIS**: смотри LICENSE в https://github.com/RustamovAkrom/JARVIS
- **Этот форк**: те же условия + дополнения от KotMir

---

## 🤝 Как помочь

### Если нашёл баг
1. Проверь в [оригинальном репо](https://github.com/RustamovAkrom/JARVIS/issues)
2. Если баг в оригинале → пиши туда
3. Если баг в лайм-теме или батниках → пиши сюда

### Если хочешь добавить фишку
1. **Для оригинальной функции** → пиши в оригинальный репо
2. **Для лайм-темы** → улучшай `style_lime.py`
3. **Для батников** → модифицируй `.bat` файлы

---

## 📞 Контакты

### Оригинальный проект
- GitHub: https://github.com/RustamovAkrom/JARVIS
- Issues: https://github.com/RustamovAkrom/JARVIS/issues

### Этот форк (Lime Hacker Edition)
- GitHub: https://github.com/Kotmir/jarvis-assistant
- Email: leula2001@outlook.com
- Discord: найди на программистских серверах

---

## 🟢 История версий

### Оригинальный JARVIS (RustamovAkrom)
- Архитектура с поддержкой множественных LLM
- Интеграция с Gemini Live
- Qt интерфейс
- Полная поддержка Windows

### Lime Hacker Edition (KotMir) v1.0
- Новая зелёная тема
- AutoPush (Python + Batch)
- Полная документация на русском
- Батники для Windows
- Attribution и thanks

---

## 🟢 Слоган

```
JARVIS Lime Hacker Edition
Форк от KotMir на основе JARVIS от RustamovAkrom

Зелёный свет, умный мозг, автоматический коммит.
Спасибо RustamovAkrom за отличный проект! 💚
```

---

**Версия**: 1.0 Lime Hacker Edition  
**Дата**: Октябрь 2026  
**Автор форка**: KotMir  
**Исходный автор**: RustamovAkrom  
**Статус**: ✅ Ready for Combat

🙏 Спасибо за отличный JARVIS, RustamovAkrom! 🟢
