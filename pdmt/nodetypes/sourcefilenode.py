import filenode
import os

class SourceFileNode(filenode.FileNode):
	""" if a source file exists then it is upto date """
	""" question: why isn't a source file ALWAYS up to date?
	answer: what if the source file went missing? We want to trigger
	an error. Well - is it this methods part to check that the file
	exists ?!? I don't think so. This methods name is called "uptodate"
	and not "verify" or something... """
	def uptodate(self,mgr,todo):
		return True;
#		return os.path.isfile(self.fname)
	def canBuild(self):
		return False
	def build(self,mgr):
		raise ValueError('dont know how to build a source file')
