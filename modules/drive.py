from telegram.ext import Updater
import requests
from urllib.parse import unquote
import re

ip_type = "ipv4"

def proxy_ipv4(url):
	payload = {}
	payload['url'] = url
	content = requests.get("https://ipv4.trolyfacebook.com/proxy/", params=payload).text
	return content
def proxy_ipv6(url):
	payload = {}
	payload['url'] = url
	content = requests.get("https://ipv6.trolyfacebook.com/proxy/", params=payload).text
	return content
def get_link_drive(id):
	data = {}
	url = 'https://docs.google.com/feeds/get_video_info?formats=ios&mobile=true&docid='+id
	if ip_type == "ipv4":
		info_video = proxy_ipv6(url)
	else:
		info_video = proxy_ipv4(url)
	if info_video !='':
		temp = info_video.split("&")
		for i in range(0, len(temp)):
			temp2 = {}
			temp2 = temp[i].split("=")
			if temp2[0] == "title":
				data['title'] = unquote(unquote(temp2[1]))
			if temp2[0] == "fmt_stream_map":
				raw = temp2[1]
				decoded = str(unquote(unquote(raw)))
				fi1080 = re.search("37\|https?:/\/[^\/]+\.google\.com/videoplayback\?id=[a-z0-9]+\&itag=[0-9]{2}\&source=webdrive\&requiressl=yes&ttl=transient\&mm=[0-9]+\&mn=[^\/]+\&ms=[^\/]+\&mv=[^\/]+\&pl=[0-9]+\&mime=video\/[a-z0-9]+\&lmt=[0-9]+\&mt=[0-9]+\&ip=[:0-9a-z]+\&ipbits=[0-9]+\&expire=[0-9]+\&sparams=[,a-z]+\&signature=[.A-Z0-9]+\&key=[a-z0-9]+\&app=explorer", decoded)
				if fi1080 is None:
					link1080 = ""
				else:
					link1080 = fi1080.group(0).replace("37|", "")
				data['1080'] = re.sub("https?:\/\/[^\/]+\.google\.com", "https://redirector.googlevideo.com", link1080)
				fi720 = re.search("22\|https?:/\/[^\/]+\.google\.com/videoplayback\?id=[a-z0-9]+\&itag=[0-9]{2}\&source=webdrive\&requiressl=yes&ttl=transient\&mm=[0-9]+\&mn=[^\/]+\&ms=[^\/]+\&mv=[^\/]+\&pl=[0-9]+\&mime=video\/[a-z0-9]+\&lmt=[0-9]+\&mt=[0-9]+\&ip=[:0-9a-z]+\&ipbits=[0-9]+\&expire=[0-9]+\&sparams=[,a-z]+\&signature=[.A-Z0-9]+\&key=[a-z0-9]+\&app=explorer", decoded)
				if fi720 is None:
					link720 = ""
				else:
					link720 = fi720.group(0).replace("22|", "")
				data['720'] = re.sub("https?:\/\/[^\/]+\.google\.com", "https://redirector.googlevideo.com", link720)
				fi480 = re.search("59\|https?:/\/[^\/]+\.google\.com/videoplayback\?id=[a-z0-9]+\&itag=[0-9]{2}\&source=webdrive\&requiressl=yes&ttl=transient\&mm=[0-9]+\&mn=[^\/]+\&ms=[^\/]+\&mv=[^\/]+\&pl=[0-9]+\&mime=video\/[a-z0-9]+\&lmt=[0-9]+\&mt=[0-9]+\&ip=[:0-9a-z]+\&ipbits=[0-9]+\&expire=[0-9]+\&sparams=[,a-z]+\&signature=[.A-Z0-9]+\&key=[a-z0-9]+\&app=explorer", decoded)
				if fi480 is None:
					link480 = ""
				else:
					link480 = fi480.group(0).replace("59|", "")
				data['480'] = re.sub("https?:\/\/[^\/]+\.google\.com", "https://redirector.googlevideo.com", link480)
				fi360 = re.search("18\|https?:/\/[^\/]+\.google\.com/videoplayback\?id=[a-z0-9]+\&itag=[0-9]{2}\&source=webdrive\&requiressl=yes&ttl=transient\&mm=[0-9]+\&mn=[^\/]+\&ms=[^\/]+\&mv=[^\/]+\&pl=[0-9]+\&mime=video\/[a-z0-9]+\&lmt=[0-9]+\&mt=[0-9]+\&ip=[:0-9a-z]+\&ipbits=[0-9]+\&expire=[0-9]+\&sparams=[,a-z]+\&signature=[.A-Z0-9]+\&key=[a-z0-9]+\&app=explorer", decoded)
				if fi360 is None:
					link360 = ""
				else:
					link360 = fi360.group(0).replace("18|", "")
				data['360'] = re.sub("https?:\/\/[^\/]+\.google\.com", "https://redirector.googlevideo.com", link360)
	else:
		data['error'] = "1"
		data['msg'] = "Không lấy được thông tin video"
	
	return data
def process(bot, update):
    if update.message.text == '/drive@AegisRobot' or update.message.text == '/drive':
        update.message.reply_text('*Syntax*: `/drive <Google Drive video url>`', 'Markdown')
    else:
        parameter = update.message.text.replace("/drive ", "")
        url1_valid = re.match("https?:\/\/drive.google.com\/open\?id=[_0-9a-zA-Z]+", parameter)
        url2_valid = re.match("https?:\/\/drive.google.com\/file\/d\/[_0-9a-zA-Z]+/view", parameter)
        id_valid = re.search("[_0-9a-zA-Z]{10,30}", parameter).group(0)
        if url1_valid or url2_valid:
        	data = get_link_drive(id_valid)
        	update.message.reply_text("[1080p]("+data['1080']+") [720p]("+data['720']+") [480p]("+data['480']+") [360p]("+data['360']+")", 'Markdown')
        else:
        	update.message.reply_text("You may have the incorrect input, check your parameter")












