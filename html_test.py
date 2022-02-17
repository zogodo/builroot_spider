#!/bin/env python3
# _*_ coding: UTF-8 _*_

from lxml import html

f = open('index.html')

doc = html.fromstring(f.read())
links = doc.xpath("//tr[not(@class='d')]/td/a[not(starts-with(@href,'..'))]")
print(len(links))
links = doc.xpath("//tr[@class='d']/td/a[not(starts-with(@href,'..'))]")
print(len(links))
