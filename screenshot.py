import base64
import requests
import os
from datetime import datetime
import webbrowser
os.getcwd()

api_key = "Get Your OWN API KEY!!! :P "
url = "http://api.imgur.com/2/upload.json"

os.system('')

filename = datetime.now().strftime('%Y-%m-%d%H:%M:%S')


t = filename + '.png'

print t
os.system('screencapture -i ' + t)
fileadd = os.getcwd() + '/' + t

fh = open(fileadd, 'rb')
base64img = base64.b64encode(fh.read())
r = requests.post(url, data={'key': api_key, 'image': base64img})
print(r.json()['upload']['links']['original'])
link = r.json()['upload']['links']['original']

os.system("echo '%s' | pbcopy" % link)
webbrowser.open(link)
