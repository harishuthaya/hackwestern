import requests
import json
import http
import os
import http.client

BASE_URL = "5yepqg.api.infobip.com"
API_KEY = "App 62c9fac6d1e9b6f0ff03f5748b70c41d-fcdd5640-3818-462d-8fbb-62092496adcb"

SENDER = "InfoSMS"
MESSAGE_TEXT = "This is a sample message"

def sms(phonenum):
    RECIPIENT = phonenum
    conn = http.client.HTTPSConnection(BASE_URL)

    payload1 = "{\"messages\":" \
            "[{\"from\":\"" + SENDER + "\"" \
            ",\"destinations\":" \
            "[{\"to\":\"" + RECIPIENT + "\"}]," \
            "\"text\":\"" + MESSAGE_TEXT + "\"}]}"

    headers = {
        'Authorization': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/sms/2/text/advanced", payload1, headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    
def getresp():
    conn = http.client.HTTPSConnection("5yepqg.api.infobip.com")
    payload = ''
    headers = {
        'Authorization': API_KEY,
        'Accept': 'application/json'
    }
    conn.request("GET", "/sms/1/inbox/reports", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


#test
sms('16472368470')