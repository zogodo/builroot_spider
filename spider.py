#!/bin/env python3
# _*_ coding: UTF-8 _*_

import re
import sys
import requests
from lxml import etree

url = 'http://sources.buildroot.net/'
url = 'https://www.openguet.cn/lab/views/login.jsp'

r = requests.get(url)

print(r.status_code)
print(r.text)

html = re.findall(r'<a.+?href="(.+?)"', r.text)
print(html)

sys.exit()

html = re.findall(r'(<body>(.*\n)+</body>)', r.text)
html = html[0][0]
print(html)

# sys.exit()

html = etree.XML(html)

html = etree.tostring(html, pretty_print=True, encoding='utf-8')

print(html)

