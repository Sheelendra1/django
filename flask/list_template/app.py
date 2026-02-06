from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def listt():
    sh = ["Sheelendra", "btech", "cse"]

    return render_template('index.html',sh=sh)