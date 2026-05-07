from models.songbooks import SongbookBugAndInfo, EngSongBook, SwSongbook, BsSongbook, DeviceInfo, MediaPath, NewsLetter
from flask_restful import reqparse, Resource, marshal_with
from app.structures import Songbook_struct, DevStruct
from app.api import db

class DevRepo(Resource):
    @marshal_with(DevStruct.DEV_INFO)
    def get(self):
        return DeviceInfo().query.all()
    
class MediaRepo(Resource):
    @marshal_with(DevStruct.MEDIA_INFO)
    def get(self):
        return MediaPath().query.all()

class NewsletterSubscription(Resource):
    @marshal_with(DevStruct.MAIL_INFO)
    def post(self):
        mails = NewsLetter().query.all()
        return mails
    
    def get(self):
      return {"message": "this path, is not found: does not exist!"}

class HeadOffice(Resource):
    def get(self):
        return {"msg": "C-2-O: SUCCESS", "state": True}
    
    def post(self):
        def checker(e, args):
            if e[1] != None and e[1] == "BUG":
                bug = SongbookBugAndInfo(detail=args["det"], bug_info=args["bug"])
                db.session.add(bug)
                try:
                    db.session.commit()
                    return True
                except:
                    db.session.rollback()
                    return False
                
            if e[1] != None and e[1] == "REQ":
                bug = SongbookBugAndInfo(detail=args["det"], bug_info=args["req"])
                db.session.add(bug)
                try:
                    db.session.commit()
                    return True
                except:
                    db.session.rollback()
                    return False
                
            if e[1] != None and e[1] == "REC":
                bug = SongbookBugAndInfo(detail=args["det"], bug_info=args["rec"])
                db.session.add(bug)
                try:
                    db.session.commit()
                    return True
                except:
                    db.session.rollback()
                    return False
            
        arg = reqparse.RequestParser()
        arg.add_argument("req")
        arg.add_argument("rec")
        arg.add_argument("bug")
        arg.add_argument("det")
        arg = arg.parse_args()
        
        if arg["req"]:
            info = arg["req"], "REQ"
            val =  checker(info, arg)
            
        elif arg["rec"]:
            info = arg["rec"], "REC"
            val =  checker(info, arg)
            
        elif arg["bug"]:
            info = arg["bug"], "BUG"
            val =  checker(info, arg)
        
        else:
            val = False
            
        return val

class InfoDispatchCenter(Resource):
    def get(self):
        return {"msg": "please make sure you are accessing this via lsb app"}
    
    @marshal_with(Songbook_struct.GENERAL_STRUCTURE)
    def post(self):
        arg = reqparse.RequestParser()
        arg.add_argument("update-lib")
        arg.add_argument("what_i_have")
        arg = arg.parse_args()

        if arg["update-lib"] == 'en':
            have_this = []
            for x in EngSongBook.query.all():
                if arg["what_i_have"]:
                    if str(x.id) in arg["what_i_have"]:
                        pass
                    else:
                        have_this.append(x)
                else:
                    have_this.append(x)
                    
            return have_this
        
        elif arg["update-lib"] == 'sw':
            have_this = []
            for x in SwSongbook.query.all():
                if arg["what_i_have"]:
                    if str(x.id) in arg["what_i_have"]:
                        pass
                    else:
                        have_this.append(x)
                else:
                    have_this.append(x)
                    
            return have_this
        
        elif arg["update-lib"] == 'bs':
            have_this = []
            for x in BsSongbook.query.all():
                if arg["what_i_have"]:
                    if str(x.id) in arg["what_i_have"]:
                        pass
                    else:
                        have_this.append(x)
                else:
                    have_this.append(x)
                    
            return have_this
        
        else:
            return {}