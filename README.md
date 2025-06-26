# Деканат-бот (Google Sheets)

## Установка зависимостей
```bash
pip install python-telegram-bot==13.15 gspread oauth2client
```

## Подготовка
1. Создайте Google таблицу с двумя колонками: Ключ и Ответ
2. Разрешите доступ вашему сервисному аккаунту (из credentials.json)
3. Укажите имя таблицы в строке: `client.open("faq_bot")`
4. Вставьте токен вашего бота от BotFather в переменную TOKEN

## Запуск
```bash
python bot.py
```