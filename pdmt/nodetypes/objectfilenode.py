import pdmt.nodetypes.sourcefilenode
import filenode
import os
import subprocess

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
			if isinstance(node,pdmt.nodetypes.sourcefilenode.SourceFileNode):
				if os.path.getmtime(node.fname)>os.path.getmtime(self.fname):
					rebuild=True
					break
		return not rebuild
	def build(self,mgr):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.fname)
		for node in mgr.deps(self):
			if isinstance(node,pdmt.nodetypes.sourcefilenode.SourceFileNode):
				args.append(node.fname)
		subprocess.check_call(args)
