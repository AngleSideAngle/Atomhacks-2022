from flask import Flask
app = Flask(__name__)

@app.route("/api/<country>")
def data(country = "US"):
    return "a";

@app.route("/")
def hello_world():
    return 

if __name__ == "__main__":
    app.run()