import os, re

with open("links.txt", "r") as websites:
    content = websites.read().splitlines()

for website in content:
    BASE_URL = website
    regex = re.findall(r'.\.(.*?)\.',website)[0]
    FOLDER_NAME = regex
    os.system('rm -r regex')
    os.system('gnome-terminal --window -e "python3 main.py"')