from bs4 import BeautifulSoup
from zhipuai import ZhipuAI
import requests, pydantic_core, pydantic
import os, datetime

def requestOver(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.content, 'lxml')
  return soup

summary = ""

def ask(content, y):
  global summary
  client = ZhipuAI(api_key="6294fdf6e42abb23a0914e137acb1a18.g1Czc1XsWW18xrjj")
  response = client.chat.completions.create(
    model="chatglm_turbo", 
    messages=[
      {"role": "user", "content": "请用三句话概括以下文本：" + content}
      ]
  )
  print(response.choices[0].message.content)
  summary += (str(y) + ". " + response.choices[0].message.content + "\n")

def download(title, url):
  soup = requestOver(url)
  tag = soup.find('div', class_= "article")
  if (tag == None):
    return 0
  title = title.replace(':', '')
  title = title.replace('"', '')
  title = title.replace('|', '')
  title = title.replace('/', '')
  title = title.replace('\\', '')
  title = title.replace('*', '')
  title = title.replace('<', '')
  title = title.replace('>', '')
  title = title.replace('?', '')

  content = ""
  for p in tag.findAll('p'):
    if (p.string != None):
      content = content + p.string
  
  y = 1
  ask(content, y)
  y += 1
  
  return 1

def crawlAll(url, cnts, MaxCount, alllist, collection):
  global summary
  if (cnts >= MaxCount):
    return
  print("Begin crowling..." + url)
  soup = requestOver(url)
  for tag in soup.findAll("a", target="_blank"):
    if (cnts >= MaxCount):
      return
    subUrl = tag.attrs["href"]
    print("Found " + subUrl)
    if tag.string != None:
      if(("https://news.sina.com.cn/" in subUrl) or ("http://news.sina.com.cn/" in subUrl)):
        alllist.append(subUrl)
        if ((subUrl not in collection)):
          collection.add(subUrl)
          try:
            if (0 == download(tag.string, subUrl)):
              crawlAll(subUrl, cnts, MaxCount, alllist, collection)
            else:
              cnts += 1
              if (cnts >= MaxCount):
                break
          except Exception as e:
            print("新闻爬取失败 url=" + url + str(e))

def use():
  collection = set()
  alllist = ["https://news.sina.com.cn/"]
  cnts = 0
  MaxCount = 4
  for n in alllist:
    target_url = n
    crawlAll(target_url, cnts, MaxCount, alllist, collection)
    
  print(summary)
  return summary

if __name__ == '__main__':
  use()

