from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import todaysWordleGame
from validation import validateRequest, checkDictionaryListWords, checkingSpecialCaractersInValidWords

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def checkWord():
    jsonData = request.get_json()
    isValid = validateRequest(jsonData)
    if not isValid:
        return "Solo se aceptan palabras de 5 letras"
    checkingRealWords = checkDictionaryListWords(isValid)
    if not checkingRealWords:
        return "Solo se aceptan palabras existentes"
    words = checkingSpecialCaractersInValidWords(checkingRealWords)
    playerAttemts = todaysWordleGame(words)
    return jsonify(playerAttemts)

if __name__ == "__main__":
    app.run(debug=True)
