from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import dictionaryRaeRandomWord, wordleGame

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def checkWord():
    answer = dictionaryRaeRandomWord()
    jsonData = request.get_json()
    payload = wordleGame(jsonData, answer)
    return jsonify(payload)
