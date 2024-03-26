from zhipuai import ZhipuAI
import datetime
import os

def ask():
  path = "spider_news/" + str(datetime.date.today()) + "/"
  i = 1
  summary = ""
  today_news = "summary/" + str(datetime.date.today()) + "新闻概括.txt"
  for filename in os.listdir(path):
    with open(path + filename, encoding='utf-8') as f:
      content = f.read()
      client = ZhipuAI(api_key="6294fdf6e42abb23a0914e137acb1a18.g1Czc1XsWW18xrjj")
      response = client.chat.completions.create(
        model="chatglm_turbo", 
        messages=[
          {"role": "user", "content": "请用三句话概括以下文本：" + content}
        ]
      )
      print(response.choices[0].message.content)
      summary += (str(i) + ". " + response.choices[0].message.content + "\n")
      i += 1
  
  with open(today_news, 'w', encoding='utf8') as file_object:
    file_object.write(summary)
  
if __name__ == '__main__': 
  ask()
      