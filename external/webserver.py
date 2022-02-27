from flask import Flask, render_template
from threading import Thread
import random
import time
import requests
import logging

app = Flask('')

@app.route('/')
def mainPage():
  return render_template('index.html')

def run():
  app.run(host='0.0.0.0',port=5000) 
def ping(target, debug):
    while(True):
        r = requests.get(target)
        if(debug == True):
            print("Status Code: " + str(r.status_code))
        time.sleep(random.randint(180,300)) #alternate ping time between 3 and 5 minutes
def awake(target ,debug=False):
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True  
    t = Thread(target=run)
    r = Thread(target=ping, args=(target,debug,))
    t.start()
    r.start()