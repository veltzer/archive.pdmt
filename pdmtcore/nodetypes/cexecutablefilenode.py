import buildfilenode
import filenode
import subprocess
import pdmtcore.types

class CExecutableFileNode(buildfilenode.BuildFileNode):
	def __init__(self,fname):
		super(CExecutableFileNode,self).__init__(fname,pdmtcore.types.t_exe)
	def build(self,mgr):
		args=[]
		args.append('gcc')
		args.append('-o')
		args.append(self.fname)
		for node in mgr.deps(self):
			if isinstance(node,filenode.FileNode):
				args.append(node.fname)
		subprocess.check_call(args)
