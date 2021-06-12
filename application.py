import sqlite3
import flask
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import os
import pandas as pd
from helpers import apology, login_required, usd
import cs50
from cs50 import SQL
from datetime import datetime

#export set FLASK_APP=application


# cd montyhacks_project
# $env:FLASK_APP = "application"
# $env:FLASK_ENV = "development"
# flask run

db = SQL("sqlite:///hospital.db")
#configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

admin = False
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin_input", methods = ["GET", "POST"])
@login_required
def admin_input():
    return render_template("admin_input.html")

@app.route("/locations", methods = ["GET", "POST"])
def locations():
    return render_template("locations.html")

@app.route("/records", methods = ["GET", "POST"])
@login_required
def records():
    return render_template("records.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)


        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        
        if str(db.execute("SELECT type FROM users WHERE username = ?", request.form.get("username"))[0]["type"]) == "Admin":
            session["type"] = rows[0]["type"]
        
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    #Just in case, clear and user sessions
    session.clear()

    #if register form is submitted
    if request.method == "POST":

        #if username
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("DOB") or not request.form.get("name") or not request.form.get("gender") or not request.form.get("type"):
            return apology("Missing credential", 400)


        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords don't match!", 400)

        else:

            if len(db.execute("SELECT * FROM users WHERE username = :username", username = request.form.get("username"))) == 0:

                hash_pwd = generate_password_hash(request.form.get("password"))

                user_id = db.execute("INSERT INTO users (username, hash, type, birth, name, gender) VALUES(:username, :hash, :type, :birth, :name, :gender)",
                                 username=request.form.get("username"), hash = hash_pwd, type = request.form.get("type"), birth = request.form.get("DOB"), name = request.form.get("name"), gender = request.form.get("gender"))
                session["user_id"] = user_id
                sign_in = True
                flash("Registered successfully!")
                return redirect("/")
            else:
                return apology("Please choose another username!", 400)
    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/login")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
