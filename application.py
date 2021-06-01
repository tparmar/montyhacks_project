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

#run this in your terminal before starting the flask application:
#export set FLASK_APP=application
#This will set the flask application



#configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
#     with sql_connect = sqlite3.connect("hospital.db")
# cursor = sql_connect.cursor()
#     cursor.execute()
    return render_template("index.html")

