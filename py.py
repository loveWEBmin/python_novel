#-*- coding:utf-8
import os
import re
novelPath="novelProject/"
def setHtmlFile(htmlCode,name):
  global novelPath
  fileName=novelPath+name+".html"
  file=open(fileName,"w")
  file.write(htmlCode)

def getText(file):
  codeStr = ""
  for line in open(file,"r"):
    codeStr+=line
  return codeStr


def getChapter(text):
  pattern = re.compile("#.+#\n")
  return pattern.findall(text)

def createIndexHtml(novelName,chapters):
  indexCode=getText("chapterInfo.html")
  indexCode=indexCode.replace("{name-name}",novelName)
  liTags="<div class=\" col-xs-12 col-sm-6 col-md-4\"><a href=\"{href-href}\">{chapter-chapter}</a></div>"
  urls=""
  for i in range(1,len(chapters)+1):
    urls+=liTags.replace("{href-href}","chapters/"+str(i)+".html").replace("{chapter-chapter}",chapters[i-1])
  indexCode = indexCode.replace("{novel-chapter}",urls)
  setHtmlFile(indexCode,"index")
def createchapter(num,chapter,content):
  indexCode=getText("chapter.html")
  indexCode=indexCode.replace("{chapter-chapter}",chapter).replace("{content-content}",content).replace("{prepage}",str(num-1)+".html").replace("{lastpage}",str(num+1)+".html")
  setHtmlFile(indexCode,"chapters/"+str(num))

def createchapters(novelFile):
  i=0
  content=""
  chapter="0"
  for line in open(novelFile,"r"):
    if(len(getChapter(line))>0):
      createchapter(i,chapter,content)
      i+=1
      chapter=line
      content=""
    else:
      content+="<p>"+line+"</p>"
  createchapter(i,chapter, content)

def main():
  global novelPath
  novelFile = "molurouqing.txt"  # 手动设置小说名字
  novelContent = getText(novelFile)
  novelName = novelFile.split(".")[0]
  novelPath += novelName+"/"
  path=novelPath+"chapters"
  if (os.path.exists(path) == False):
    os.makedirs(path)

  print "novelPath:"+path  #输出生成小说路径

  chapters=getChapter(novelContent)
  print len(chapters)    #输出小说章节

  createIndexHtml(novelName,chapters)

  createchapters(novelFile)


if __name__ == '__main__':

  main()


