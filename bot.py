import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from dotenv import load_dotenv


# Авторизация и загрузка данных из Google Sheets
def load_faq_from_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("api-project-808198968975-d4e3da9b7665.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("faq")  # Название вашей таблицы
    worksheet = sheet.sheet1
    data = worksheet.get_all_records()

    faq = {}
    for row in data:
        key = row["Ключ"].strip().lower()
        answer = row["Ответ"].strip()
        faq[key] = answer
    return faq

faq = load_faq_from_gsheet()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я деканат-бот Gsheets. Задайте вопрос, например: 'Где взять справку?'")

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()
    response = "Извините, не нашёл ответ. Попробуйте другими словами."

    for keyword, answer in faq.items():
        if keyword in user_message:
            response = answer
            break

    update.message.reply_text(response)

def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()