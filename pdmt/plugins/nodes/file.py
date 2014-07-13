import pdmt.api # for NodeType
import os.path # for getmtime, isfile

'''
A file node. Anything which is a file should mix in this one.
'''

class NodeType(pdmt.api.NodeType):
	def __init__(self, name=None):
		super().__init__(name=name, proto='file')
	def get_lmt(self):
		# if the file does not exist then lmt is very old:
		if not os.path.isfile(self.name):
			return float(0)
		else:
			return pdmt.utils.fileops.getmtime(self.name)
