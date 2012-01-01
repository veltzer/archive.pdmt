import filenode
import os

class ObjectFileNode(filenode.FileNode):
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
			if isinstance(node,pdmt.nodetypes.filenode.SourceFileNode):
				if os.path.getmtime(node.fname)>os.path.getmtime(self.fname):
					rebuild=True
					break
		return not rebuild
	def build(self):
		raise ValueError('dont know how to build an object file')
