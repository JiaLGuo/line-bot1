from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
