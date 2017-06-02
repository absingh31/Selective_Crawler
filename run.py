import subprocess

with open("links.txt", "r") as websites:
    content = websites.read().splitlines()

for website in content:
    BASE_URL = website
    execute = str('python3 main.py ' + BASE_URL +' 2>/dev/null')
    subprocess.call(execute, shell=True)