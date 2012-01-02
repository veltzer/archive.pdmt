import buildnode
import filenode
import os

""" a mixin class """
class BuildFileNode(filenode.FileNode,buildnode.BuildNode):
	pass
