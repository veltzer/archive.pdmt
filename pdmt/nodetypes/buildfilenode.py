import buildnode
import filenode
import os
import pdmt.utils.fileops

"""
	a mixin class representing a node that can be build (not source)
"""
class BuildFileNode(filenode.FileNode,buildnode.BuildNode):
	def clean(self):
		if os.path.isfile(self.m_fname):
			print('unlinking [{name}]'.format(name=self.m_fname))
			pdmt.utils.fileops.unlink(self.m_fname)
