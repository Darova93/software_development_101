from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
@cross_origin()
def hello_world():
    response = {
        "message": "Hello",
        "code": 200,
        "author": "kubix"
    }
    return jsonify(response)
