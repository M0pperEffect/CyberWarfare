from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import random

app = Flask(__name__)

SCOREBOARD_FILE = "scoreboard.json"

# Load or initialize scoreboard
try:
    with open(SCOREBOARD_FILE, "r") as f:
        scoreboard = json.load(f)
except:
    scoreboard = {"red": 0, "blue": 0}

# Join route
@app.route("/join", methods=["GET"])
def join():
    team = random.choice(["red", "blue"])
    return render_template("join.html", team=team)

# Submit action (attack/defense)
@app.route("/submit", methods=["POST"])
def submit():
    team = request.form.get("team")
    points = int(request.form.get("points", 1))
    scoreboard[team] += points
    with open(SCOREBOARD_FILE, "w") as f:
        json.dump(scoreboard, f)
    return redirect(url_for("leaderboard"))

# Leaderboard
@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", scoreboard=scoreboard)

# Homepage
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
