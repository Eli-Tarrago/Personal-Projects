#!/usr/bin/env python3
import requests

with open('/home/arlion/SecLists/Discovery/Web-Content/burp-parameter-names.txt') as f:
    Lines = f.readlines()

for line in Lines:
    print(line)
    r = requests.get('http://167.71.143.20:31831/{{' + line + '}}')
    print(r.text)
    print(r.url)

