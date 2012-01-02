import filenode
import subprocess

class ObjectFileNode(filenode.FileNode):
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
