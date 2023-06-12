from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os
from googletrans import Translator
import json

API_KEY=''
os.environ['OPENAI_Key'] = API_KEY
openai.api_key = os.environ['OPENAI_Key']

app = Flask(__name__)
CORS(app)

with open('intents.json', 'r') as f:
    intents = json.load(f)

def get_response(text):
    for q, a in intents.items():
        if text.lower() in q.lower():
            return a
    response = openai.Completion.create(engine='text-davinci-003', prompt=text, max_tokens=200)
    response = response['choices'][0]['text']
    return response

@app.route("/predict", methods=["POST", "GET"])
def predict():
    text = request.get_json().get("message")
    trans = Translator()
    lang = trans.detect(text).lang
    
    if lang == 'ta':
        text = trans.translate(text, dest='en').text
        response = trans.translate(get_response(text), dest='ta').text
        message = {"answer": response}
        return jsonify(message)

    elif lang == 'ml':
        text = trans.translate(text, dest='en').text
        response = trans.translate(get_response(text), dest='ml').text
        message = {"answer": response}
        return jsonify(message)

    elif lang == 'te':
        text = trans.translate(text, dest='en').text
        response = trans.translate(get_response(text), dest='te').text
        message = {"answer": response}
        return jsonify(message)

    elif lang == 'hi':
        text = trans.translate(text, dest='en').text
        response = trans.translate(get_response(text), dest='hi').text
        message = {"answer": response}
        return jsonify(message)

    elif lang == 'kn':
        text = trans.translate(text, dest='en').text
        response = trans.translate(get_response(text), dest='kn').text
        message = {"answer": response}
        return jsonify(message)

    elif text.lower() in ['hello', 'hi', 'hlo', 'hiii', 'hii']:
        response = "Hello there, how can I help you?"
        message = {"answer": response}
        return jsonify(message)

    elif text.lower() in ['ok', 'thank you', 'yes']:
        response = "Ok sir/mam. Any other queries? I am happy to help."
        message = {"answer": response}
        return jsonify(message)

    elif text.lower() in ['what is your name']:
        response = " I am APK bot"
        message = {"answer": response}
        return jsonify(message)    

    else:
        t = trans.translate(text)
        response = get_response(t.text)
        message = {"answer": response}
        return jsonify(message)

@app.route("/")
def chatbot():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
