from flask import Flask, jsonify
from flask_cors import CORS

from src.util.constants import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [PERSONAL_SITE_URL, "*"]}})


@app.get("/ping")
def ping():
    return jsonify({"message": "pong"}), 200


from src.controller import *
