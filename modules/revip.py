from telegram.ext import Updater
import requests
import re
from netaddr import IPNetwork, IPAddress
import socket
import json

def process(bot, update):
    if update.message.text == '/revip@AegisRobot' or update.message.text == '/revip':
        update.message.reply_text('*Syntax*: `/revip IP or domain`', 'Markdown')
    else:
        parameter = update.message.text.replace("/revip ", "")
        ip_valid = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", parameter)
        domain_valid = re.match("(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)", parameter)
        if ip_valid or domain_valid:
            ip = socket.gethostbyname(parameter)
            if IPAddress(ip) in IPNetwork("103.21.244.0/22") or IPAddress(ip) in IPNetwork("103.22.200.0/22") or IPAddress(ip) in IPNetwork("103.31.4.0/22") or IPAddress(ip) in IPNetwork("104.16.0.0/12") or IPAddress(ip) in IPNetwork("108.162.192.0/18") or IPAddress(ip) in IPNetwork("131.0.72.0/22") or IPAddress(ip) in IPNetwork("141.101.64.0/18") or IPAddress(ip) in IPNetwork("162.158.0.0/15") or IPAddress(ip) in IPNetwork("172.64.0.0/13") or IPAddress(ip) in IPNetwork("173.245.48.0/20") or IPAddress(ip) in IPNetwork("188.114.96.0/20") or IPAddress(ip) in IPNetwork("190.93.240.0/20") or IPAddress(ip) in IPNetwork("197.234.240.0/22") or IPAddress(ip) in IPNetwork("198.41.128.0/17") or IPAddress(ip) in IPNetwork("199.27.128.0/21"):
                update.message.reply_text('This IP or domain is a host of CloudFlare network. I cannot reverse ip lookup')
            else:
                url = "http://domains.yougetsignal.com/domains.php?remoteAddress="
                headers = {'content-type': 'application/json'}
                content = requests.post(url+ip, headers=headers).text
                decoded = json.loads(content)
                number = int(decoded['domainCount'])
                domains = ""
                for i in range(0, number - 1):
                    domains = domains + (decoded['domainArray'][i][0]) + "\n"
                update.message.reply_text(domains)
        else:
            update.message.reply_text("You may have the incorrect input, check your parameter")