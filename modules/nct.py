from telegram.ext import Updater
import requests
import re

def process(bot, update):
    if update.message.text == '/nct@AegisRobot' or update.message.text == '/nct':
        update.message.reply_text('*Syntax*: `/nct <url>`', 'Markdown')
    else:
        parameter = update.message.text.replace("/nct ", "")
        url_valid = re.match("https?:\/\/www\.nhaccuatui\.com\/bai-hat\/[-a-z]+\.[a-z0-9A-Z]+\.html", parameter)
        if url_valid:
            content = requests.get(parameter).text
            xml = re.search("https?:\/\/www\.nhaccuatui\.com\/flash\/xml\?key1=[0-9a-z]{30,40}", content).group(0)
            headers = {'content-type': 'application/xml'}
            xmlcontent = requests.get(xml, headers=headers).text
            link = re.search("https?:/\/[^\/]+\.nixcdn\.com\/[-_\/a-zA-Z0-9]+\.mp3", xmlcontent).group(0)
            update.message.reply_text("[Download]("+link+")", 'Markdown')
        else:
            update.message.reply_text("You may have the incorrect input, check your parameter")

