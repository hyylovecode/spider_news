import json,hashlib,time,reply,download,ask
import xml.etree.ElementTree as ET
import datetime,pydantic



def main_handler(event, context):
    if event['httpMethod'] == 'GET':
        return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "plain/text"},
        "body": event['queryString']['echostr']
        }

    if event['httpMethod'] == 'POST':
        webData = event['body']
        xmlData = ET.fromstring(webData)

        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        MsgType = xmlData.find('MsgType').text
        MsgId = xmlData.find('MsgId').text
        Msgcontent = xmlData.find('Content').text

        toUser = FromUserName
        fromUser = ToUserName
        content = '部署成功！'#公众号返回给用户的消息

        nowtime = str(int(time.time()))
        
        if Msgcontent == "今日新闻":
            download.use()
            ask.ask()
            with open("summary/" + str(datetime.date.today()) + "新闻概括.txt", 'r', encoding='utf8') as f:
                content = f.read()
        
        return reply.ReplyText(toUser,fromUser,nowtime,MsgType,content)
