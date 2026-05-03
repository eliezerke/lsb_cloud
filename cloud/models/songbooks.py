from app.api import db

class EngSongBook(db.Model):
    __tablename__ = "songbook_en"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    lyrics = db.Column(db.String(100000), unique=True)
    key = db.Column(db.String(10), unique=True)
    
    
class SwSongbook(db.Model):
    __tablename__ = "songbook_sw"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    lyrics = db.Column(db.String(100000), unique=True)
    key = db.Column(db.String(10), unique=True)
    
    def to_json(self):
        return {"id": self.id, "title": self.title, "lyrics": self.lyrics, "key": self.key}
    
class BsSongbook(db.Model):
    __tablename__ = "songbook_bs"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    lyrics = db.Column(db.String(100000), unique=True)
    key = db.Column(db.String(10), unique=True)
    
    def to_json(self):
        return {"id": self.id, "title": self.title, "lyrics": self.lyrics, "key": self.key}
    
class SongbookBugAndInfo(db.Model):
    __tablename__ = "bug_and_info"
    id = db.Column("id", db.Integer, primary_key=True)
    bug_info = db.Column(db.String, unique=False)
    detail = db.Column(db.String, unique=False)

    def __repr__(self):
        return f"BUG: {self.bug_info}"
    
class RegDwn(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    counts = db.Column(db.Integer)

class DeviceInfo(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    platform = db.Column(db.String(20))
    user_agent = db.Column(db.String)
    ext = db.Column(db.Integer)

    def __repr__(self):
        return f"EXT: {self.ext}, USER_AGENT: {self.user_agent}, PLATFORM: {self.platform}"