import asyncio
import datetime
import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Bot
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, ConversationHandler, filters, MessageHandler
)

# load secrets
BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_ID = int(os.getenv("TELEGRAM_ID"))
REDDIT_APP_TOKEN = os.getenv("REDDIT_APP_TOKEN")

# logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def validate_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == TELEGRAM_ID:
        return True
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="invalid user ID"
        )
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if await validate_user(update, context):

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="I'm the RedditBot! I do Reddit stuff!"
        )



if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # connect handlers here
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()