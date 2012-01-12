import operation

class InstallAptSite(operation.Operation):
	def __init__(self,p_name,p_description,p_node1,p_node2,p_node3):
		super(InstallAptSite,self).__init__(p_name,p_description)
		self.m_node1=p_node1
		self.m_node2=p_node2
		self.m_node3=p_node3
	def run(self,nodes):
		print('running')
