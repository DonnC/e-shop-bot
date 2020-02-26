'''
@author:  Donald C
@created: some-what a while ago
@updated: recently
@github : @DonnC
@project: whatsapp bot (template) using twilio and heroku
@license: free as the wind
'''

from flask import Flask, request, jsonify
from datetime import datetime as dtime
from src.handler import BotHandler

app   = Flask(__name__)

now_  = dtime().now().strftime("%H:%M")

# JUST A TIP!!!!!!!!!!!
# heroku free dyno refresh dyno after 30 min of inactivity
# so its file system starts anew, deleting your updated files like logs
# it starts a new with same file as in your initial github repo
# well...thats the price for using free services. 😜

@app.route('/', methods=['GET'])
def home():
    #TODO Add nice dashboard / NEVER
    status = {
        "bot-server": "OK",
        "server-time": now_,
        "star-follow-at": "https://github.DonnC"
    }
    return jsonify(status)

@app.route('/whatsapp', methods=['GET', 'POST'])     # bot webhook
def whatsapp():
    from_ = request.values.get('From')               # from twilio API
    body_ = request.values.get('Body').strip()
    body_ = body_.lower()

    if body_:
        BotEngine   = BotHandler(body_, from_)
        BotEngine.runBotHandler()

    return ''

if __name__ == "__main__":
    # flag to False when going to production
    app.run(debug=True)