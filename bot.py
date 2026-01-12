import requests
from bs4 import BeautifulSoup
import time
import os

TOKEN = os.getenv("7835502369:AAHKWF5LPCrF2G8Tgh8HRjOfjgEshmBjKrs")
CHAT_ID = os.getenv("5838817768")
URL = "https://www.stwdo.de/wohnen/aktuelle-wohnangebote"

last_state = ""

def send_message(msg):
    api = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(api, data={"chat_id": CHAT_ID, "text": msg})

while True:
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    state = soup.get_text()

    if last_state and state != last_state:
        send_message("🚨 hbat aaredh tawa fisaa!\n" + URL)

    last_state = state
    time.sleep(300)
