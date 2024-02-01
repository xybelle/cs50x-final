from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

app = Flask(__name__)

db = SQL("sqlite:///gds.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

CLASSES = ["ballet", "tap", "hiphop"]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        c = request.form.get("class")
        if c not in CLASSES:
            return apology("Please select class")
        fname = request.form.get("fname")
        sname = request.form.get("sname")
        guardian = request.form.get("parent-guardian")
        email = request.form.get("email")
        pw = request.form.get("password")
        conf = request.form.get("confirmation")

        # Check if email is already registered
        stu = db.execute("SELECT email FROM students WHERE email = ?", email)
        existing_stu = stu[0] if stu else None

        # Check if stu already exists in the database
        if existing_stu:
            return apology("Email already registered. Please try logging in instead.")
        # Validate submission
        elif not fname or not sname:
            return apology("Please enter your name")
        # Ensure password is entered
        elif not pw:
            return apology("Please enter a password")
        # Ensure password and confirmation matches
        elif pw != conf:
            return apology("Passwords do not match")

        # Hash password
        hashed_pw = generate_password_hash(pw, method='pbkdf2', salt_length=2)

        try:
            # Remember students
            db.execute("INSERT INTO students (fname, sname, email, hash, guardian) VALUES (?, ?, ?, ?, ?)",
                        fname, sname, email, hashed_pw, guardian)

            # Update classes database
            db.execute("INSERT INTO enrolments_summer2023 (name, student_id) VALUES (?, ?)", c, session["user_id"])
        except Exception as e:
            print(e)
            return apology("Something went wrong. Please try again.")

        rows = db.execute("SELECT * FROM students WHERE email = ?", email)
        session["user_id"] = rows[0]["id"]

        # Confirm registration
        return redirect("/home")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("Please enter your email", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please enter your password", 403)

        # Query database for email
        rows = db.execute(
            "SELECT * FROM students WHERE email = ?", request.form.get("email")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("Invalid email and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to index
        return redirect("/home")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to index
    return redirect("/")

@app.route("/classes", methods=["GET"])
def classes():
    return render_template("classes.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    name = db.execute("SELECT guardian FROM students WHERE id =?", session["user_id"])

    enrolled_in = db.execute("SELECT name FROM enrolments_summer2023 WHERE student_id = ?", session["user_id"])


    return render_template("home.html", name=name, c=enrolled_in)
