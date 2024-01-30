from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///gds.db")

CLASSES = ["Ballet", "Jazz", "Hip-Hop"]

@app.route("/", methods=["POST"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    fname = request.form.get("fname")
    sname = request.form.get("sname")
    email = request.form.get("email")
    if not fname or sname or email or "class" in CLASSES:
        return render_template("error.html", message="Something is missing")

    # Remember students
    db.execute("INSERT INTO students (fname, sname, email) VALUES (?, ?, ?)", fname, sname, email)

    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM")
    return render_template("confirmation.html")
