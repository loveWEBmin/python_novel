#-*- coding:utf-8
import os
import re
import requests
from lxml import etree

#-*- 如果想获取 其他网站的小说,只需自己改动  xpath 的匹配代码

def requestHtml(url,tryTimes=1):  #通过网址 获取对应网页的html 源代码
  try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print url
    return r.text
  except:
    if(tryTimes<5):               #获取失败之后是否重新获取,三次机会
      return requestHtml(url,tryTimes+1)
    else:
      print "requestHtml() have a error"
      return ""


def parseChapters(url):           #获取对应网页的小说章节 ,网址必须是https://www.2kxs.com/的小说对应的小说章节页面
  htmlCode=requestHtml(url)       
  html=etree.HTML(htmlCode)
  chapters=html.xpath('//ul[@class="mulu_list"]/li/a/text()')
  hrefs=html.xpath('//ul[@class="mulu_list"]/li/a/@href')
  return chapters,hrefs


def parseContent(url):           #获取对应网页的小说正文部分 ,网址必须是https://www.2kxs.com/的小说对应的小说的阅读页面
  htmlCode=requestHtml(url)
  html=etree.HTML(htmlCode)
  content=html.xpath('//div[@id="htmlContent"]/text()')
  txt=""
  for i in content:
    txt+=i+"\n"
  return txt

def autoParseTxt(url,txtName):  #自动生成对应的txt小说文档 
  chapters, urls = parseChapters(url)
  txtContext=""
  for i in range(len(urls)):
    content=parseContent(url+urls[i])
    txtContext+="#"+chapters[i]+"#\n"+content
    print i*1.0/len(urls)*100,"%"
  file=open(txtName+".txt","w")
  file.write(txtContext.encode("utf-8"))


def main():
  url="https://www.ybdu.com/xiaoshuo/9/9824/"
  txtName="jidushanbojue"
  autoParseTxt(url,txtName)


if __name__ == '__main__':
  main()


