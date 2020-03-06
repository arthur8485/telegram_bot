import re
import requests

def get_ngrok_url():

    req = requests.get("http://127.0.0.1:80/status")
    matches = re.search(r"https://[a-z0-9]+.ngrok.io", req.text, re.IGNORECASE)
    return matches.group(0)