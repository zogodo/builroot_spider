#!/bin/env python3
# _*_ coding: UTF-8 _*_

from genericpath import getsize
import os
import re
import sys
from tqdm import tqdm
from os.path import dirname
from urllib.parse import urljoin, urlparse, urlsplit
from xml.sax.handler import feature_external_ges
import requests
from lxml import html

# from multiprocessing import Manager, Pool

import asyncio
import aiohttp
sem = asyncio.Semaphore(25)

url = 'http://sources.buildroot.net/'

pbar = tqdm(total=1)

async def get_raw(url):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return await resp.read()

async def get_size(url):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.head(url) as resp:
                if resp.status == 200:
                    return resp.content_length

async def get_raw_ensure(url, retries=20):
    while retries > 0:
        try:
            retries -= 1
            content = await get_raw(url)
            pbar.update(1)
            return content
        except KeyboardInterrupt:
            raise
        except:
            pass

async def Download(url):
    fName = urlparse(url).path
    fName = "img" + fName
    if os.path.exists(fName):
        pbar.update(1)
        # return
        if os.path.getsize(fName) == await get_size(url):
            # tqdm.write("already exist  %s" % fName)
            return
        else:
            tqdm.write("file is broken %s" % fName)
    data = await get_raw_ensure(url)
    tqdm.write("len=%10d %s" % (len(data), fName))
    try:
        os.makedirs(dirname(fName))
    except:
        pass
    with open(fName, 'wb') as f:
        f.write(data)

# a = resp.read()
# x = await a

# url = 'https://www.openguet.cn/lab/views/login.jsp'
# url = 'https://zogodo.github.io/'

# r = requests.get(url)

async def Anls(url):
    res = await get_raw_ensure(url)
    doc = html.fromstring(res.decode('utf-8'))
    links = doc.xpath("//tr[not(@class='d')]/td/a[not(starts-with(@href,'..'))]")
    xx = [Download(urljoin(url, link.get('href'))) for link in links]
    links = doc.xpath("//tr[@class='d']/td/a[not(starts-with(@href,'..'))]")
    yy = [Anls(urljoin(url, link.get('href'))) for link in links]
    zz = xx + yy
    pbar.total += len(zz)
    await asyncio.wait(zz)
    # arr = []
    # for link in links:
    #     arr.append(Anls(urljoin(url, link)))
    # await asyncio.wait(arr)

    # for link in links:
    #     Anls(url)

coroutine = Anls(url)
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

sys.exit()


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

