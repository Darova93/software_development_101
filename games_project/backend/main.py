from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/v0.1/api/wordle/checkword", methods=["POST"])
@cross_origin()
def hello_world():
    print(request.get_json())
    response = {
        
        "message": "Hello",
        "code": 200,
        "author": "kubixxx"
    }
    return jsonify(response)
