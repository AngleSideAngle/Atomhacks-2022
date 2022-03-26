from ast import Str
import string
from flask import Flask, jsonify, render_template, request
from itsdangerous import NoneAlgorithm
from soupsieve import escape
app = Flask(__name__)

@app.route("/api")
def data(country = "US"):
    country = request.args.get("country", "US")
    day = request.args.get("day", 1)
    data = {
        "cases" : "tba"
    }
    return jsonify(data);

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
