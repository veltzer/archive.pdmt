import pdmt.api
import os

class NodeType(pdmt.api.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name=name, proto=proto)
		self.proto='file'
	def uptodate(self,todo):
		# if the file does not exist then rebuild is needed
		if not os.path.isfile(self.name):
			return False
		# the file exists so lets compare dates, all source files
		# must exist
		rebuild=False
		for node in self.getDeps():
			if node in todo:
				rebuild=True
				break
			if isinstance(node,pdmt.plugins.node.file.NodeType):
				if os.path.getmtime(node.name)>os.path.getmtime(self.name):
					rebuild=True
					break
		return not rebuild
