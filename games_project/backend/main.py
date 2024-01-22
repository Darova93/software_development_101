from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import WordleAttempt

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

answer = "MARIA"

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def hello_world():
    jsonData = request.get_json()
    guess = jsonData['word']
    aComparison = WordleAttempt(guess,answer)
    response = {
        "correctLetterIndices" : aComparison.correctLetterIndices,
        "missplacedLetterIndices" : aComparison.missplacedLetterIndices,
        "wrongLetterIndices" : aComparison.wrongLetterIndices
    }
    return jsonify(response)
