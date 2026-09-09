from app import app
from flask import render_template, redirect, flash, request

@app.route("/")
def home():
    return render_template('index.html')