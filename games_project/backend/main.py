from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import todaysWordleGame

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def checkWord():
    jsonData = request.get_json()
    playerAttemts = todaysWordleGame(jsonData)
    return jsonify(playerAttemts)
