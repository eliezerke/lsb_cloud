from drivers.driver import HeadOffice, InfoDispatchCenter, DevRepo, MediaRepo, NewsletterSubscription, MsgFeedbacks
from app.api import api

api.add_resource(HeadOffice, "/api/lsb/")
api.add_resource(DevRepo, "/api/dev/")
api.add_resource(MediaRepo, "/api/dev/paths")
api.add_resource(NewsletterSubscription, "/api/dev/mails/")
api.add_resource(MsgFeedbacks, "/api/dev/messages/")
api.add_resource(InfoDispatchCenter, "/api/lsb/update/")