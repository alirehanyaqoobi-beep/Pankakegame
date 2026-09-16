# GameHub Template

A minimal Flask template for a website that hosts browser games.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Project structure

```
game-website/
├── app.py                  # Flask app + game registry
├── requirements.txt
├── templates/
│   ├── base.html            # shared layout (nav/footer)
│   ├── index.html           # home page / game grid
│   ├── game_page.html       # individual game page
│   ├── about.html
│   └── 404.html
├── static/
│   ├── css/style.css
│   ├── js/script.js         # shared JS
│   ├── js/games/            # put per-game JS files here
│   └── images/              # thumbnails, etc.
└── games/                   # (optional) put game-specific Python logic here
```

## Adding a new game

1. Add a thumbnail image to `static/images/`.
2. Add an entry to the `GAMES` list in `app.py`:

```python
{
    "slug": "snake",
    "title": "Snake",
    "description": "Classic snake game.",
    "thumbnail": "images/snake.png",
},
```

3. It will automatically show up on the home page and be reachable at `/games/snake`.
4. Build the actual game — either:
   - Write client-side JS in `static/js/games/snake.js` and reference it from `game_page.html` (or create a dedicated template if the game needs custom layout), or
   - Add server-side game logic in Python and extend `app.py` with any extra routes/API endpoints it needs.

## Notes

- This is a template — `example-game` in the registry is just a placeholder to show the layout working.
- Styling lives in `static/css/style.css` and uses CSS variables at the top for easy re-theming.
