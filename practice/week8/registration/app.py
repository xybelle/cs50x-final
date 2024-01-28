from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
    if request.method == "POST":
        name = request.form.get("name", "world")
        return render_template("register.html", name=name)
    else:
        return render_template("index.html")
