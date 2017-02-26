from telegram.ext import Updater
import requests
import re
import json

def process(bot, update):
    if update.message.text == '/fb@AegisRobot' or update.message.text == '/fb':
        update.message.reply_text('*Syntax*: `/fb <Facebook video url>`', 'Markdown')
    else:
        parameter = update.message.text.replace("/fb ", "")
        url_valid = re.match("https?:\/\/www\.facebook\.com\/[\w\s]{6,30}\/videos\/[0-9]{10,18}\/(.+)?", parameter)
        id = re.search("([0-9]{10,18})", parameter).group(1)
        if url_valid:
            s = requests.get('https://www.facebook.com/video/embed?video_id='+id).text
            content = s[s.index('"videoData":[')+len('"videoData":['):s.index('],"minQuality":')]
            decoded = json.loads(content)
            if not decoded['sd_src']:
                update.message.reply_text("[HD quality]("+decoded['hd_src']+")", 'Markdown')
            elif not decoded['hd_src']:
                update.message.reply_text("[SD quality]("+decoded['sd_src']+")", 'Markdown')
            else:
                update.message.reply_text("[SD quality]("+decoded['sd_src']+")\n[HD quality]("+decoded['hd_src']+")", 'Markdown')
        else:
            update.message.reply_text("You may have the incorrect input, check your parameter")