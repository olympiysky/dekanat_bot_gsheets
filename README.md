# Деканат-бот (Google Sheets)

## Установка зависимостей
```bash
pip install python-telegram-bot==13.15 gspread oauth2client
```

## Подготовка
1. Создайте Google таблицу с двумя колонками: Ключ и Ответ
2. Разрешите доступ вашему сервисному аккаунту (из credentials.json)
Когда вы работаете с Google Sheets через API, вы используете сервисный аккаунт Google. Для этого аккаунта создаётся специальный файл — credentials.json, который содержит ключи и идентификаторы для доступа к Google API.
Что нужно сделать:
В Google Cloud Console вы создаёте сервисный аккаунт и скачиваете credentials.json.
В этом файле есть поле client_email — это адрес сервисного аккаунта, например:
my-bot-123@my-project.iam.gserviceaccount.com
Откройте вашу Google таблицу (ту, с которой будет работать бот).
Нажмите "Файл" → "Доступ" (или "Share"/"Поделиться").
Введите адрес сервисного аккаунта (из поля client_email в credentials.json) и дайте ему права "Редактор" (или хотя бы "Чтение", если бот только читает данные).
Сохраните изменения.

Как В Google Cloud Console создать сервисный аккаунт и скачиваете credentials.json.
1. Перейдите в Google Cloud Console
https://console.cloud.google.com/
2. Создайте или выберите проект
Вверху страницы нажмите на выпадающий список рядом с названием проекта и выберите существующий проект или нажмите New Project для создания нового.
3. Включите Google Sheets API
В левом меню выберите APIs & Services → Library.
В строке поиска введите Google Sheets API.
Кликните по найденному результату и нажмите Enable.
4. Создайте сервисный аккаунт
В левом меню выберите IAM & Admin → Service Accounts.
Нажмите Create Service Account (сверху).
Введите имя (например, "dekanat-bot") и, при необходимости, описание.
Нажмите Create and Continue.
5. Назначение ролей (можно пропустить)
На шаге Grant this service account access to project можно ничего не выбирать, просто нажмите Continue.
6. Завершите создание
На шаге Grant users access to this service account просто нажмите Done.
7. Скачайте credentials.json
В списке сервисных аккаунтов найдите только что созданный аккаунт.
В колонке Actions (три точки справа) выберите Manage keys.
Нажмите Add Key → Create new key.
Выберите JSON и нажмите Create.
Файл credentials.json скачается на ваш компьютер.
8. Поместите credentials.json в папку с вашим проектом
Не забудьте:
Email сервисного аккаунта (например, my-bot-123@my-project.iam.gserviceaccount.com) используйте для предоставления доступа к Google Таблице (через "Share" → "Editor" или "Viewer").
credentials.json — это приватный файл, не выкладывайте его в открытый доступ.
3. Укажите имя таблицы в строке: `client.open("faq_bot")`
4. Вставьте токен вашего бота от BotFather в переменную TOKEN


creds = ServiceAccountCredentials.from_json_keyfile_name("api-project-808198968975-d4e3da9b7665.json"
Именить на свой 


gspread.exceptions.APIError: APIError: [403]: Google Drive API has not been used in project ... or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=...

Что это значит:
Для работы с Google Sheets через gspread требуется не только включить Google Sheets API, но и Google Drive API.
Сейчас Google Drive API для вашего проекта не включён, поэтому возникает ошибка 403 (доступ запрещён).
Нажмите кнопку "Enable" (или "Включить" — если интерфейс на русском).
Подождите пару минут
Иногда активация занимает 1-2 минуты.
Запустите ваш бот снова
Ошибка должна исчезнуть.

## Запуск
```bash
python bot.py
```