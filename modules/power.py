from telegram.ext import Updater
def process(bot, update):
    update.message.reply_text("I'm ready. Waiting for commands, sir")