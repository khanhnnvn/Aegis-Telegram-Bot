#!/usr/bin/env python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from sys import exit, version_info
import logging
import config

if version_info < (3,):
  raise RuntimeError('You need to run Python 3')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Main program
updater = Updater(config.TOKEN)

def main():
    dp = updater.dispatcher

    # Add more command to handle
    from modules import power
    dp.add_handler(CommandHandler("power", power.process))
    from modules import revip
    dp.add_handler(CommandHandler("revip", revip.process))
    from modules import nmap
    dp.add_handler(CommandHandler("nmap", nmap.process))
    from modules import webin
    dp.add_handler(CommandHandler("wig", webin.process))
    from modules import mp3
    dp.add_handler(CommandHandler("mp3", mp3.process))
    from modules import fb
    dp.add_handler(CommandHandler("fb", fb.process))
    from modules import drive
    dp.add_handler(CommandHandler("drive", drive.process))
    from modules import nct
    dp.add_handler(CommandHandler("nct", nct.process))

    
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

if __name__ == '__main__':
    main()
