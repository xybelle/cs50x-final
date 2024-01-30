import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT stock FROM stocks WHERE user_id = ?), session["user_id"]
    shares_owned =
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # When requested via GET
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        shares = request.form.get("shares")
        if stock == None:
            return apology("Symbol does not exist")

        elif shares is None or shares == "" or int(shares) <= 0:
            return apology("Enter the number of shares you wish to buy")
        else:
            user = session["user_id"]
            rows = db.execute("SELECT * FROM users WHERE id = ?", user)
            cash = rows[0]["cash"]
            buy_price = int(stock['price']) * int(shares)
            bal = cash - buy_price

            if bal < 0:
                return apology("Not enough balance")
            else:
                id = rows[0]["id"]

                # Add transaction to database
                db.execute("INSERT INTO stocks (user_id, stock, shares) VALUES (?, ?, ?)", id, stock['symbol'], int(shares))

                # Update cash balance
                db.execute("UPDATE users SET cash = ? WHERE id = ?", bal, id)

    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # When requested via GET
    if request.method == "GET":
        return render_template("quote.html")

    # When form is submitted via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")

        stock = lookup(symbol)

        # If lookup is unsuccessful
        if stock == None:
            return apology("Symbol does not exist")

        # If lookup is successful
        else:
            return render_template("quoted.html", price=stock['price'], symbol=stock['symbol'])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # When form is submitted via POST
    if request.method == "POST":
        name = request.form.get("username")
        pw = request.form.get("password")
        conf = request.form.get("confirmation")
        user = db.execute("SELECT username FROM users WHERE username = ?", name)
        existing_user = user[0] if user else None

        # Check if user already exists in the database
        if existing_user:
            return apology ("Username already exists")
        # Ensure username is entered
        if not name:
            return apology("Please enter a username")
        # Ensure password is entered
        elif not pw:
            return apology("Please enter a password")
        # Ensure password and confirmation matches
        elif pw != conf:
            return apology("Passwords do not match")

        # Hash the password
        hashed_pw = generate_password_hash(pw, method='pbkdf2', salt_length=len(pw))

        # Add user to database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, hashed_pw)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    # When requested via GET
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
