# Automated API to add repl to Uptimerobot to keep alive repl. 
# Implement by adding "import uptimerobot" => main.py
# Requires keys.txt with API keys.
# https://uptimerobot.com/api/
import requests
import time
import os
f = open("keys.txt", 'r') # Uptimerobot API keys (1 key = 50 repl)
_key = f.readline()
_url = f"https://{os.environ['REPL_SLUG']}.{os.environ['REPL_OWNER']}.repl.co"
_name = "NoRussia_REPL"
while True:
  keys = _key.replace("\n", '')
  url = "https://api.uptimerobot.com/v2/newMonitor"
  payload = f"api_key={keys}&format=json&type=1&url={_url}&friendly_name={_name}"
  headers = {'cache-control': "no-cache", 'content-type': "application/x-www-form-urlencoded"}
  response = requests.request("POST", url, data=payload, headers=headers)
  if '"stat": "ok",' in response.text: 
    break
  elif 'already exists' in response.text:
    break
  else: 
    _key = next(f)