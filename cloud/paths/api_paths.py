from drivers.driver import HeadOffice, InfoDispatchCenter, DevRepo
from app.api import api

api.add_resource(HeadOffice, "/api/lsb/")
api.add_resource(DevRepo, "/api/dev/")
api.add_resource(InfoDispatchCenter, "/api/lsb/update/")