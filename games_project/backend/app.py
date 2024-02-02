from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from wordle import todaysWordleGame
from validation import validateRequest, checkDictionaryListWords, checkSpecialCaractersInValidWords

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def checkWord():
    wordleRequest = request.get_json()
    isValid = validateRequest(wordleRequest)
    
    if not isValid:
        return wordleRequest
    checkingRealWords = checkDictionaryListWords(isValid)
    if not checkingRealWords:
        return wordleRequest
    
    playerAttemts = todaysWordleGame(checkingRealWords)
    
    return jsonify(playerAttemts)

if __name__ == "__main__":
    app.run(debug=True)
