import sqlite3
import flask
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import os
import mysql.connector
from mysql.connector import Error
import pandas as pd
from helpers import apology, login_required, usd

#run this in your terminal before starting the flask application:
#export set FLASK_APP=application
#for you guys, its just set FLASK_APP=application

# Nihaal- I need to do this to run it. It is the only way to change the environment to development in powershell.
# cd montyhacks_project
# $env:FLASK_APP = "application"
# $env:FLASK_ENV = "development"
# flask run
# test
#This will set the flask application
con = sqlite3.connect("hospital.db", check_same_thread = False)
cursor = con.cursor()

#configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

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

@app.route("/locations", methods = ["GET", "POST"])
def locations():
    return render_template("locations.html")

@app.route("/record", methods = ["GET", "POST"])
def records():
    return render_template("records.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    # session.clear()
    # if request.method == "POST":

    #     if not request.form.get("username"):
    #         return apology("Missing username!", 400)


    #     elif not request.form.get("password"):
    #         return apology("Missing password!", 400)


    #     elif request.form.get("password") != request.form.get("confirmation"):
    #         return apology("Passwords don't match!", 400)

    #     else:

    #         if len(cursor.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))) == 0:

    #             hash_pwd = generate_password_hash(request.form.get("password"))

    #             user_id = cursor.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
    #                              username=request.form.get("username"), hash=hash_pwd)
    #             session["user_id"] = user_id

    #             flash("Registered successfully!")
    #             return redirect("/")
    #         else:
    #             return apology("Please choose another username!", 400)

    return render_template("register.html")
