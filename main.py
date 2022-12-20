from flask import Flask, render_template, request, redirect, send_file
from extractors.alba import extract_alba_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {

}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    return render_template("search.html")

app.run("127.0.0.1:5000")