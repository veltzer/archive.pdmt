import pdmt.api # for EventHandler
import os # for environ

class EventHandler(pdmt.api.EventHandler):
	def respond(self,pdmt,data,eventtype):
		if os.environ.get('PDMT_DEBUG') != None:
			print(pdmt,data,eventtype)
