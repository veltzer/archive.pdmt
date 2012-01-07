import buildfilenode
import filenode
import subprocess
import pdmtcore.types

class ObjectFileNode(buildfilenode.BuildFileNode):
	def __init__(self,p_fname):
		super(ObjectFileNode,self).__init__(p_fname,pdmtcore.types.t_object)
	def build(self,mgr):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.fname)
		for node in mgr.deps(self):
			if isinstance(node,filenode.FileNode):
				args.append(node.fname)
		subprocess.check_call(args)
