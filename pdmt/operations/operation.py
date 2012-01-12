class Operation(object):
	def __init__(self,p_name,p_description):
		self.m_name=p_name
		self.m_description=p_description
	def getName(self):
		return self.m_name
	def run(self,nodes):
		print('operation empty')
