from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import WordleComparison

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

answer = "MARIA"

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def checkWord():
    jsonData = request.get_json()
    playerGuess = jsonData['word']
    currentWordleComparison = WordleComparison(playerGuess,answer)
    response = {
        "correctLetterIndices" : currentWordleComparison.correctLetterIndices,
        "missplacedLetterIndices" : currentWordleComparison.missplacedLetterIndices,
        "wrongLetterIndices" : currentWordleComparison.wrongLetterIndices
    }
    return jsonify(response)
