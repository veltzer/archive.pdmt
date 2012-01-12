import buildnode
import filenode
import os

"""
	a mixin class representing a node that can be build (not source)
"""
class BuildFileNode(filenode.FileNode,buildnode.BuildNode):
	def clean(self):
		if os.path.isfile(self.m_fname):
			print('unlinking [{name}]'.format(name=self.m_fname))
			os.unlink(self.m_fname)
