from flask import Flask, render_template, request

app = Flask(__name__)

STUDENTS = {}

CLASSES = ["Ballet", "Jazz", "Hip-Hop"]

@app.route("/", methods=["POST"])
    return render_template("index.html", class=CLASSES)

@app.route("/register", methods=["POST"])
def register():

    #fname = request.form.get("fname")
    #if not name:
    #    return render_template("error.html", message="Missing name")
    if not request.form.get("fname") or not request.form.get("sname")
            or not request.form.get("email") or not in CLASSES:
        return render_template("error.html", message="Missing email")
    return render_template("success.html")

    STUDENTS[fname]

    return redirect("/confirmation")

@app.route("/confirmation")
def confirmation():
     return render_template("confirmation.html", students=STUDENTS)
