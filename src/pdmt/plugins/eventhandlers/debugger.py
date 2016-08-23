import pdmt.api # for EventHandler
import os # for environ

class EventHandler(pdmt.api.EventHandler):
    def respond(self,data=None,eventtype=None):
        if os.environ.get('PDMT_DEBUG') != None:
            print(data,eventtype)
