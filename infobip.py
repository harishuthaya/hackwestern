import requests
import json
import http
import os

BASE_URL = "5yepqg.api.infobip.com"
API_KEY = os.environ.get("INFOBIP_API_KEY")
#if code breaks, check here

SENDER = "InfoSMS"


def sms(phonenum, url):
    RECIPIENT = phonenum
    MESSAGE_TEXT = "Your doctor is ready to meet with you! Join your live video call at: " + url
    conn = http.client.HTTPSConnection(BASE_URL)

    payload_dict = {
        "messages": [
            {
                "from": SENDER,
                "destinations": [
                    {"to": RECIPIENT}
                ],
                "text": MESSAGE_TEXT
            }
        ]
    }
    payload1 = json.dumps(payload_dict)

    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload1, headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
