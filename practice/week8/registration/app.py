from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name"):
        return "failure"
