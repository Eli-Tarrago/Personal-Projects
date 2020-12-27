#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup 
import hashlib

url = 'http://178.128.38.142:31225'

r1 = requests.get(url)

soup = BeautifulSoup(r1.text, "lxml") 
  
# Get the whole h3 tag 
tag = soup.h3
  
# Get the attribute, use the hashlib lib to encode it. using hexdigest() makes the md5 hash the 
# most reconizable version of a md5hash.
md5Encypted = hashlib.md5(tag.text.encode()).hexdigest()

# Post reqest, data para is set to key: hash. Cookies param is to that of the original requests.
# r1.cookies = 'PHPSESSID=e22s8nieaskom08h8b0vprmk72; path=/'
# <RequestsCookieJar[<Cookie PHPSESSID=ogf6l8vlef5rhq0qcvg4jeulk1 for 178.128.38.142/>]>
r = requests.post(url, data={'hash': md5Encypted}, cookies=r1.cookies)
print(r.text)
