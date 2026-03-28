from flask_restful import fields

class Songbook_struct():
    GENERAL_STRUCTURE = {
        "id": fields.Integer, 
        "title": fields.String,
        "lyrics": fields.String,
        "key": fields.String
    }