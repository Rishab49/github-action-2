from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "hello from rishab raj #5000"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

