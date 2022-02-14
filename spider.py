#!/bin/env python3
# _*_ coding: UTF-8 _*_

import re
import sys
from os import mkdir
from os.path import dirname
from urllib.parse import urljoin, urlparse, urlsplit
from xml.sax.handler import feature_external_ges
import requests
from lxml import html

# from multiprocessing import Manager, Pool

import asyncio
import aiohttp
sem = asyncio.Semaphore(10)

url = 'http://sources.buildroot.net/'

async def get_raw(url):
    async with sem: 
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return await resp.read()

async def Download(url):
    data = await get_raw(url)
    fName = urlparse(url).path
    mkdir(dirname(fName))
    f = open(fName, 'wb')
    f.write(data)

# a = resp.read()
# x = await a

# url = 'https://www.openguet.cn/lab/views/login.jsp'
# url = 'https://zogodo.github.io/'

# r = requests.get(url)

f = open('index.html')

g_links = []
async def Anls(url):
    res = await get_raw(url)
    doc = html.fromstring(res.decode('utf-8'))
    links = doc.xpath("//tr[not(@class='d')]/td/a")
    g_links.extend(links)
    xx = [Download(urljoin(url, link)) for link in links]
    links = doc.xpath("//tr[@class='d']/td/a")
    yy = [Anls(urljoin(url, link)) for link in links]
    await asyncio.wait(xx + yy)
    # arr = []
    # for link in links:
    #     arr.append(Anls(urljoin(url, link)))
    # await asyncio.wait(arr)

    # for link in links:
    #     Anls(url)

coroutine = Anls(url)
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)


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

