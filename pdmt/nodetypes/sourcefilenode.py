import filenode
import os

class SourceFileNode(filenode.FileNode):
	def __init__(self,fname):
		self.fname=fname
	def __repr__(self):
		return self.fname
	def uptodate(self,mgr):
		return os.path.isfile(self.fname)
	def build(self,mgr):
		raise ValueError('dont know how to build a source file')
