from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def index():
    return "hello, world"
