from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import WordleComparison
from public.import_text import WordOfTheDay

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

dictionary = WordOfTheDay("./public/palabras_rae.txt")
answer = dictionary.randomWord()

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def checkWord():
    jsonData = request.get_json()
    playerGuess = jsonData['word']
    currentWordleComparison = WordleComparison(playerGuess, answer)
    response = {
        "Correct word": answer,
        "correctLetterIndices" : currentWordleComparison.correctLetterIndices,
        "missplacedLetterIndices" : currentWordleComparison.missplacedLetterIndices,
        "wrongLetterIndices" : currentWordleComparison.wrongLetterIndices
    }
    return jsonify(response)
