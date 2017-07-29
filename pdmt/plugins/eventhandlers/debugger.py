import pdmt.api
import os


class EventHandler(pdmt.api.EventHandler):
    def respond(self, data=None, eventtype=None):
        if os.environ.get('PDMT_DEBUG') is not None:
            print(data, eventtype)
