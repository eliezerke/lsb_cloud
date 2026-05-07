from app.api import app, db
from paths import api_paths, web_paths
from models.models import EngSongBook, BsSongbook, SwSongbook, SongbookBugAndInfo

with app.app_context():
    db.create_all()

app = app    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)