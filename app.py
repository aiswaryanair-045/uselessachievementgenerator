from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

ACHIEVEMENTS = [
    {
        "title": "Master of Delayed Decisions",
        "description": "You completed a task so efficiently that it was almost definitely unnecessary.",
        "rarity": "Epic",
    },
    {
        "title": "Professional Time Traveler",
        "description": "You spent 20 minutes reinventing a process that already worked perfectly.",
        "rarity": "Rare",
    },
    {
        "title": "Legendary Procrastinator",
        "description": "You created a new system to avoid doing the original task for a while longer.",
        "rarity": "Legendary",
    },
    {
        "title": "Certified Snack Break Expert",
        "description": "You turned a tiny pause into a full strategic break with remarkable confidence.",
        "rarity": "Common",
    },
    {
        "title": "Founder of Productive Looking Busy",
        "description": "You performed the kind of activity that looked useful from a distance and felt meaningless up close.",
        "rarity": "Rare",
    },
    {
        "title": "Grandmaster of Unnecessary Complexity",
        "description": "You solved a simple problem with enough extra steps to deserve a medal for confusion.",
        "rarity": "Epic",
    },
    {
        "title": "Official Overthinker",
        "description": "You considered every option, ignored the obvious answer, and still called it a win.",
        "rarity": "Common",
    },
    {
        "title": "Ambassador of Low Priority",
        "description": "You handled the least important thing with the most dramatic energy possible.",
        "rarity": "Legendary",
    },
]

RarityXP = {
    "Common": 25,
    "Rare": 50,
    "Epic": 90,
    "Legendary": 150,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "Friend").strip() or "Friend"

    achievement = random.choice(ACHIEVEMENTS)
    rarity = achievement["rarity"]
    xp = RarityXP.get(rarity, 25)

    return jsonify(
        {
            "name": name,
            "title": achievement["title"],
            "description": achievement["description"],
            "rarity": rarity,
            "xp": xp,
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
