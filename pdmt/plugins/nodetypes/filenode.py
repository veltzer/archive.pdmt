import pdmt.api
import os

class NodeType(pdmt.api.NodeType):
	def __init__(self,p_fname,p_type):
		super().__init__(p_type)
		self.m_fname=p_fname
	def __repr__(self):
		return self.m_fname+','+self.m_type
	def uptodate(self,todo):
		# if the file does not exist then rebuild is needed
		if not os.path.isfile(self.m_fname):
			return False
		# the file exists so lets compare dates, all source files
		# must exist
		rebuild=False
		for node in self.getDeps():
			if node in todo:
				rebuild=True
				break
			if isinstance(node,pdmt.plugins.nodetypes.filenode.NodeType):
				if os.path.getmtime(node.m_fname)>os.path.getmtime(self.m_fname):
					rebuild=True
					break
		return not rebuild
