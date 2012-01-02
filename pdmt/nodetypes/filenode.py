import node
import os

class FileNode(node.Node):
	def __init__(self,fname):
		self.fname=fname
	def __repr__(self):
		return self.fname
	def uptodate(self,mgr):
		# if the file does not exist then rebuild is needed
		if not os.path.isfile(self.fname):
			return False
		# the file exists so lets compare dates, all source files
		# must exist
		rebuild=False
		for node in mgr.deps(self):
			if isinstance(node,FileNode):
				if os.path.getmtime(node.fname)>os.path.getmtime(self.fname):
					rebuild=True
					break
		return not rebuild
