import pdmt.plugins.nodes.buildfile
import pdmt.plugins.nodes.cfile
import pdmt.utils.subproc
import pdmt.types

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	def build(self):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.name)
		args.append(self.getSourceOfType(pdmt.plugins.nodes.cfile.NodeType).name)
		pdmt.utils.subproc.check_call(args)
