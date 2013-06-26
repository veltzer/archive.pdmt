"""
This is the base class of all node handlers within the system
"""

class NodeHandler(object):
	def respond(self,mgr,node,eventtype):
		raise ValueError('must override')
