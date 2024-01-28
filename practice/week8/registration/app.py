from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
    if request.method == "POST":
        name = request.form.get("name", "world")
        return render_template("register.html", name=name)
    else:
        return render_template("index.html")

@app.route("/register")
def register():
    if not request.form.get("name"):
        return "failure"
