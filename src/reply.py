import time

def ReplyText(toUser,fromUser,nowtime,MsgType,content):
    XmlForm = f"""
        <xml>
            <ToUserName><![CDATA[{toUser}]]></ToUserName>
            <FromUserName><![CDATA[{fromUser}]]></FromUserName>
            <CreateTime>{nowtime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{content}]]></Content>
        </xml>
        """

    return {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {"Content-Type": "application/xml"},
    "body": XmlForm
    }