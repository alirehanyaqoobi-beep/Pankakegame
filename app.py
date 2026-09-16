"""
Game Website Template
----------------------
A simple Flask app that serves as a hub for browser games.
Add new games by:
  1. Dropping their static assets in /static or /games
  2. Adding an entry to the GAMES list below
  3. Creating a template for the game page (or reusing game_page.html)
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Game registry — add one dict per game here as you build them out.
# ---------------------------------------------------------------------------
GAMES = [
    {
        "slug": "example-game",
        "title": "Example Game",
        "description": "A placeholder game to show how the template works.",
        "thumbnail": "images/placeholder.png",
    },
    # {
    #     "slug": "snake",
    #     "title": "Snake",
    #     "description": "Classic snake game.",
    #     "thumbnail": "images/snake.png",
    # },
]


def get_game(slug):
    return next((g for g in GAMES if g["slug"] == slug), None)


@app.route("/")
def home():
    return render_template("index.html", games=GAMES)


@app.route("/games/<slug>")
def game_page(slug):
    game = get_game(slug)
    if game is None:
        abort(404)
    return render_template("game_page.html", game=game)


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
