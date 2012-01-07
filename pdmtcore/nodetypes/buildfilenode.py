import buildnode
import filenode
import os

"""
	a mixin class representing a node that can be build (not source)
"""
class BuildFileNode(filenode.FileNode,buildnode.BuildNode):
	def clean(self):
		if os.path.isfile(self.fname):
			os.unlink(self.fname)
