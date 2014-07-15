import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.objectfile # for NodeType
import pdmt.utils.subproc # for check_call

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	def __init__(self, name=None):
		super().__init__(name=name)
		self.add_edge(self.getConfigNode('LDFLAGS'))
	def filebuild(self):
		args=[]
		args.append('gcc')
		args.append('-o')
		args.append(self.name)
		cfg_LDFLAGS=self.getConfig('LDFLAGS')
		if cfg_LDFLAGS!='':
			args.append(cfg_LDFLAGS)
		for node in self.getSourcesOfType(pdmt.plugins.nodes.objectfile.NodeType):
			args.append(node.name)
		pdmt.utils.subproc.check_call(args)
