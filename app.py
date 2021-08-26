from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessages
)

app = Flask(__name__)
#權杖
#秘密
line_bot_api = LineBotApi('M2r+nNXhDnmoR2JC/j4jbU3W3BvlMV6lNNrZQ24+WANC6iDXGPzT0Zt+6gTyKuX+5AcmwJi7nocgk4tLB5C2NC1P9FuPFF0qNm4Q/0QijVSDtl29/qa7J+6JEXv4hm9tmqWutCxkjCKvOr93J9tdmAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ec32c44b8d5835504e5d2431aa6d79f7')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply='不好伊速，偶不豬道你在說什麼?'
    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626502'
        )
        return

    if msg in ['妳是誰', '名字']:
        reply = '張巧巧'
    elif msg in '住哪':
        reply = '偶素桃園平鎮小公主'
    elif msg in '電話':
        reply = '偶男友說不可以隨便給人喔'
    elif msg in '生日':
        reply = '9/14 記得送我禮物^^'
    elif msg in ['身高']:
        reply = '153cm'
    elif msg in ['體重']:
        reply = '52kg'
    elif msg in ['單身嗎']:
        reply = '偶有很愛的男朋友嚕^^'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()
