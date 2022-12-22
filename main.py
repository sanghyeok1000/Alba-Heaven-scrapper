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
    search_job = extract_alba_jobs()
    db = search_job
    return render_template("search.html", db=db)

@app.route("/export")
def export():
    save_to_file(db, db)
app.run("127.0.0.1")