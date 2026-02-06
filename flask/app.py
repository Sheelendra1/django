from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from db import init_db

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            return "All fields are required"

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )

        conn.commit()
        conn.close()

        return "Data saved successfully"
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)

