"""
This is the base class of all operations within the system
"""

class Operation(object):
	def __init__(self,p_name,p_description):
		self.m_name=p_name
		self.m_description=p_description
	def getName(self):
		return self.m_name
	def getDescription(self):
		return self.m_description
	def run(self,nodes):
		raise ValueError('must override the operation')
