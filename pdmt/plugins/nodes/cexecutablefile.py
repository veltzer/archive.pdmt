import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.objectfile # for NodeType
import pdmt.utils.subproc # for check_call

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	def filebuild(self):
		args=[]
		args.append('gcc')
		args.append('-o')
		args.append(self.name)
		for node in self.getSourcesOfType(pdmt.plugins.nodes.objectfile.NodeType):
			args.append(node.name)
		pdmt.utils.subproc.check_call(args)
