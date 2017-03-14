from django.shortcuts import render
from django.http import HttpResponse
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from lineBot.settings import LINE_CAT, LINE_CS
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    line_bot_api = LineBotApi(LINE_CAT)
    webhook_parser = WebhookParser(LINE_CS)
    signature = ""
    if request.META.get("X-Line-Signature"):
        signature = request.META.get("X-Line-Signature")
    body = request.body

    try:
        events = webhook_parser.parse(body, signature)
        for event in events:
            print event
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    except InvalidSignatureError:
        print "Masuk Sini"
        return HttpResponse("Signature invalid")

    return HttpResponse("")