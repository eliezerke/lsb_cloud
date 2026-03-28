from app.api import app as application, db
from paths import api_paths, web_paths
from models.songbooks import EngSongBook, BsSongbook, SwSongbook, SongbookBugAndInfo

with application.app_context():
    db.create_all()
    
application.run(debug=True)