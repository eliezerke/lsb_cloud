from models.songbooks import EngSongBook, SwSongbook
from app.api import app

with app.app_context():
    c = EngSongBook().query.all()
    d = SwSongbook().query.all()
    
PATHS = {
    "exe": "/lsb/download/exe",
    "rar": "/lsb/download/zip",
    "apk": "/lsb/download/apk",
    "pdf": "/lsb/guide/pdf",
    "data": {"en": c, "sw": d},
}