import os
import re
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.params import Header
from starlette.requests import Request
from models.message_request import MessageRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage
from skills import *
from skills import skills

app = FastAPI()

load_dotenv()

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

def get_message(request: MessageRequest):
    for pattern, skill in skills.items():
        if re.match(pattern, request.intent):
            return skill(request)
    request.intent = '{not_match}'
    return skills['{not_match}'](request)

@app.post("/api/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature. Please check your channel access token/channel secret.")
    return 'OK'
    
@handler.add(event=MessageEvent, message=TextMessage)
def handle_message(event):
    msg_request = MessageRequest()
    msg_request.intent = event.message.text
    msg_request.message = event.message.text
    msg_request.user_id = event.source.user_id
    
    func = get_message(msg_request)
    line_bot_api.reply_message(event.reply_token, func)
