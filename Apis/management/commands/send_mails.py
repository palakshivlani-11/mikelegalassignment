import threading
import time
import requests
from django.core.management.base import BaseCommand
from Apis.models import Subscriber

MAILGUN_API_KEY = 'pubkey-b10a6955e1e871f6337e73201eb0c707'
MAILGUN_DOMAIN = 'sandbox00b35b2903264c82acff513ad2320688.mailgun.org'

BASE_EMAIL_TEMPLATE = """
    <html>
        <head></head>
        <body>
            <h1>{subject}</h1>
            <p>{preview_text}</p>
            <p>Read the full article <a href="{article_url}">here</a>.</p>
            <p>{html_content}</p>
            <p>{plain_text_content}</p>
            <p>Published Date: {published_date}</p>
        </body>
    </html>
"""