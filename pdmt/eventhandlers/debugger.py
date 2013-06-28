import pdmt.eventhandler
import os # for environ

class EventHandler(pdmt.eventhandler.EventHandler):
	def respond(self,pdmt,data,eventtype):
		if os.environ.get("PDMT_DEBUG") != None:
			print(pdmt,data,eventtype)
