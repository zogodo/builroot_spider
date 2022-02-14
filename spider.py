#!/bin/env python3
# _*_ coding: UTF-8 _*_

import re
import sys
import requests
from lxml import html

import asyncio
import aiohttp

url = 'http://sources.buildroot.net/'
# url = 'https://www.openguet.cn/lab/views/login.jsp'
# url = 'https://zogodo.github.io/'

# r = requests.get(url)

f = open('index.html')



doc = html.fromstring(f.read())
print(doc)

for a in doc.xpath("//a"):
    href = a.get('href')


len(doc.xpath("//tr[@class='d']/td/a"))
len(doc.xpath("//tr[not(@class='d')]/td/a"))

# doc.xpath("//tr/td/a")[0].get("href")

# html = re.findall(r'<a.+?href="(.+?)"', r.text)
# print(html)

sys.exit()

# html = re.findall(r'(<body>(.*\n)+</body>)', r.text)
# html = html[0][0]
# print(html)

# sys.exit()

html = html.XML(html)

html = html.tostring(html, pretty_print=True, encoding='utf-8')

print(html)

