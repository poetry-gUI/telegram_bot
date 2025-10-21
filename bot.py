from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv

# Токен вашего бота, полученный у BotFather
load_dotenv()

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("Показать картинку 📸", callback_data='show_image')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Нажмите кнопку, чтобы увидеть картинку.', reply_markup=reply_markup)

async def button_callback(update: Update, context):
    query = update.callback_query
    if query.data == 'show_image':
        # Отправляем картинку пользователю
        with open('img/1580x1140.jpg', 'rb') as image_file:
            await query.answer()
            await query.edit_message_media(media=image_file.read())

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Обработчик нажатия кнопок
    application.add_handler(CallbackQueryHandler(button_callback))
    
    print("Bot started...")
    application.run_polling()

if __name__ == '__main__':
    main()