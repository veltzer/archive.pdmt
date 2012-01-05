import node
import os

class FileNode(node.Node):
	def __init__(self,p_fname,p_type):
		super(FileNode,self).__init__(p_type)
		self.fname=p_fname
	def __repr__(self):
		return self.fname+','+self.m_type
	def uptodate(self,mgr,todo):
		# if the file does not exist then rebuild is needed
		if not os.path.isfile(self.fname):
			return False
		# the file exists so lets compare dates, all source files
		# must exist
		rebuild=False
		for node in mgr.deps(self):
			if node in todo:
				rebuild=True
				break
			if isinstance(node,FileNode):
				if os.path.getmtime(node.fname)>os.path.getmtime(self.fname):
					rebuild=True
					break
		return not rebuild
