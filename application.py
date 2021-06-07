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
    return render_template("register.html")

#make user input part of sql table
s_id = input('User ID: ')
s_name = input('Name:')
s_birth = input('Birthdate:')
cursor.execute("""
INSERT INTO database_code(id, name, birth)
VALUES (?,?,?,?)
""", (s_id, s_name,s_birth))
con.commit ()
print ( 'Data entered successfully.' )
con.close ()
if (con):
  con.close()
  print("\nThe SQLite connection is closed.")