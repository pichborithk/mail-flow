from flask import jsonify

from src import app


@app.errorhandler(500)
def handling_500(err):
    return jsonify({"name": err.name, "message": err.description}), 500
