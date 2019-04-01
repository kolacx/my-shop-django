# -*- coding: utf-8 -*-

import requests
from django.conf import settings


TELEGRAM_SEND_MESSAGE_API_URL = "https://api.telegram.org/bot%s/sendMessage" % settings.TELEGRAM_BOT_ID


def send_message(text, chat_id=settings.TELEGRAM_CHAT_ID):
    response = requests.post(TELEGRAM_SEND_MESSAGE_API_URL, data={'text': text, 'chat_id': chat_id})
    data = response.json()
    if data.get('ok', False) is False:
        print("error")
