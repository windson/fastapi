import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.params import Header
from starlette.requests import Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage
from linebot.models.send_messages import TextSendMessage

app = FastAPI()

load_dotenv()

line_bot_api = LineBotApi(os.getenv('LineChannelAccessToken'))
handler = WebhookHandler(os.getenv('LineChannelSecret'))

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
    msg = TextSendMessage(text=f'你輸入了: {event.message.text}')
    line_bot_api.reply_message(event.reply_token, msg)