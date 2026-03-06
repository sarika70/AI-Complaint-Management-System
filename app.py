from flask import Flask, render_template, request
import sqlite3
from model import predict_category

app = Flask(__name__)

# Insert complaint into database
def insert_complaint(text, category):
    conn = sqlite3.connect("complaints.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        category TEXT
    )
    """)

    cur.execute("INSERT INTO complaints(text, category) VALUES (?,?)", (text, category))

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():

    if request.method == "POST":

        complaint = request.form["complaint"]

        category = predict_category(complaint)

        insert_complaint(complaint, category)

        return render_template("submit.html", category=category)

    return render_template("submit.html")


@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("complaints.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM complaints")

    data = cur.fetchall()

    conn.close()

    return render_template("dashboard.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)