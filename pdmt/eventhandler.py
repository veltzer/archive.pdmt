"""
This is the base class of all event handlers within the system
"""

class EventHandler(object):
	def respond(self,pdmt,data,eventtype):
		raise ValueError('must override')
