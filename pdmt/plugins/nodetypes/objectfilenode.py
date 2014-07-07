import pdmt.plugins.nodetypes.buildfilenode
import pdmt.plugins.nodetypes.cfilenode
import pdmt.utils.subproc
import pdmt.types

class NodeType(pdmt.plugins.nodetypes.buildfilenode.NodeType):
	def build(self):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.name)
		args.append(self.getSourceOfType(pdmt.plugins.nodetypes.cfilenode.NodeType).name)
		pdmt.utils.subproc.check_call(args)
