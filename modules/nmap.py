from telegram.ext import Updater
import requests
import re
import os
import socket

def process(bot, update):
    if update.message.text == '/nmap@AegisRobot' or update.message.text == '/nmap':
        update.message.reply_text('*Syntax*: `/nmap IP or domain`', 'Markdown')
    else:
        parameter = update.message.text.replace("/nmap ", "")
        ip_valid = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", parameter)
        domain_valid = re.match("(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)", parameter)
        if ip_valid or domain_valid:
            ip = socket.gethostbyname(parameter)
            update.message.reply_text("Please be patient! The result will be sent when the scan is complete")
            os.system('nmap '+ip+' > output.txt')
            file = open("output.txt", "r")
            update.message.reply_text(file.read())
        else:
            update.message.reply_text("You may have the incorrect input, check your parameter")