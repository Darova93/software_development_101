from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import WordleComparison

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

answer = "MARIA"

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def hello_world():
    jsonData = request.get_json()
    playerGuess = jsonData['word']
    aComparison = WordleComparison(playerGuess,answer)
    response = {
        "correctLetterIndices" : aComparison.correctLetterIndices,
        "missplacedLetterIndices" : aComparison.missplacedLetterIndices,
        "wrongLetterIndices" : aComparison.wrongLetterIndices
    }
    return jsonify(response)
