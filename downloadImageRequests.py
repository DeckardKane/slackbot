import os
import requests
import errno
import itertools
import platform

content_filePath = "content/content.jpg"
style_filePath = "style/style.jpg"

# Example

# test urls:
# https://static.gamespot.com/uploads/screen_kubrick/1577/15776161/3402571-0539057649-33987.jpg
# https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg

content_input_url = input("Please provide a URL for a content image: ")
style_input_url = input("Please provide a URL for a style image: ")

content_filename = content_input_url.split("/")[-1]
content_filePath = "/home/paperspace/Desktop/slackbot/content/{}".format(content_filename)
print(content_filePath)
r = requests.get(content_input_url, timeout=0.5)

if r.status_code == 200:
    with open(content_filePath, 'wb') as f:
        f.write(r.content)

style_filename = style_input_url.split("/")[-1]
style_filePath = "/home/paperspace/Desktop/slackbot/style/{}".format(style_filename)
print(style_filePath)
r = requests.get(style_input_url, timeout=0.5)

if r.status_code == 200:
    with open(style_filePath, 'wb') as f:
        f.write(r.content)
