from telegram.ext import Updater
import requests
import re
import json

def process(bot, update):
    if update.message.text == '/mp3@AegisRobot' or update.message.text == '/mp3':
        update.message.reply_text('*Syntax*: `/mp3 <url>`', 'Markdown')
    else:
        parameter = update.message.text.replace("/mp3 ", "")
        url_valid = re.match("(https?:\/\/)?mp3\.zing\.vn\/bai-hat\/[\w\d\-]+/([\w\d]{8})\.html", parameter)
        string_valid = re.search("([A-Z0-9]{8})", parameter).group(1)
        if url_valid:
            content = requests.get('http://phulieuminhkhang.com/images/Sanpham/api.php?parameter='+string_valid).text
            decoded = json.loads(content)
            update.message.reply_text("*Song:* `"+decoded['title']+"`, *Artist:* `"+decoded['artist']+"`\n[128Kbps]("+decoded['link_download']['128']+")\n[320Kbps]("+decoded['source']['320']+")", 'Markdown')
        else:
            update.message.reply_text("You may have the incorrect input, check your parameter")