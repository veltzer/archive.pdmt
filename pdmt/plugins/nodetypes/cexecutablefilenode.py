import pdmt.plugins.nodetypes.buildfilenode # for NodeType
import pdmt.plugins.nodetypes.objectfilenode # for NodeType
import pdmt.utils.subproc # for check_call

class NodeType(pdmt.plugins.nodetypes.buildfilenode.NodeType):
	def build(self):
		args=[]
		args.append('gcc')
		args.append('-o')
		args.append(self.name)
		for node in self.getSourcesOfType(pdmt.plugins.nodetypes.objectfilenode.NodeType):
			args.append(node.name)
		pdmt.utils.subproc.check_call(args)
