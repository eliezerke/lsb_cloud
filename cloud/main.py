from app.api import app, db
from paths import api_paths, web_paths
from flask import url_for, redirect
from models.models import (
    EngSongBook, 
    BsSongbook, 
    SwSongbook, 
    SongbookBugAndInfo,
    DeviceInfo,
    Feedback,
    MediaPath,
    NewsLetter,
    RegDwn
    )

with app.app_context():
    db.create_all()

@app.route("/lsb/guide", methods=["POST", "GET"])
def guide():
    return redirect("/static/pdf/livesongbook.pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)