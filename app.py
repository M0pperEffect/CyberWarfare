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
    scoreboard = scoreboard = {"red": [], "blue": []}


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form.get("name")
        team = request.form.get("team")  # or random.choice(["red", "blue"])
        scoreboard[team].append({"name": name, "score": 0})
        with open(SCOREBOARD_FILE, "w") as f:
            json.dump(scoreboard, f)
        return redirect(url_for("leaderboard"))
    return render_template("join.html")

#submit
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    points = int(request.form.get("points", 1))
    team = request.form.get("team")

    # find the player in the team
    for player in scoreboard[team]:
        if player["name"] == name:
            player["score"] += points
            break

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
    app.run(debug=True, host="0.0.0.0")
