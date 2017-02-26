from telegram.ext import Updater
import re
from wig.wig import wig

def process(bot, update):
    if update.message.text == '/wig@AegisRobot' or update.message.text == '/wig':
        update.message.reply_text('*Syntax*: `/wig domain`', 'Markdown')
    else:
        parameter = update.message.text.replace("/wig ", "")
        domain_valid = re.match("(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)", parameter)
        if domain_valid:
            update.message.reply_text("Please be patient! The result will be sent when the scan is complete")
            w = wig(url=parameter)
            w.run()
            results = w.get_results()
            if not results:
                update.message.reply_text("An error has been occurred. I can't scan this domain")
            else:
                str1 = "\n".join(str(x) for x in results)
                update.message.reply_text(str1)  
        else:
            update.message.reply_text("You may have the incorrect input, check your parameter")