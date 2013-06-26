import pdmt.eventhandler

class EventHandler(pdmt.eventhandler.EventHandler):
	def respond(self,pdmt,data,eventtype):
		print(pdmt,data,eventtype)
