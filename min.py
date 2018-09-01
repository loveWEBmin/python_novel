#-*- coding:utf-8
import os
import re
import requests
from lxml import etree

r=requests.get("https://www.ybdu.com/xiaoshuo/9/9824/1933555.html")
html = etree.HTML(r.content)
#content = html.xpath("//ul[@class]/li/a/text()")
content = html.xpath('//div[@id="htmlContent"]/text()')
txt = ""
# for i in content:
#   if(i!='\r\n'):
#     print i
for i in content:
  print i+"\n\n"
