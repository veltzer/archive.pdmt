import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.objectfile # for NodeType

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.add_edge(self.getConfigNode('LDFLAGS'))
	def filebuild(self, nbp):
		args=[]
		args.append('gcc')
		args.append('-o')
		args.append(self.name)
		cfg_LDFLAGS=self.getConfig('LDFLAGS')
		if cfg_LDFLAGS!='':
			args.append(cfg_LDFLAGS)
		for node in self.getSourcesOfType(pdmt.plugins.nodes.objectfile.NodeType):
			args.append(node.name)
		nbp.addCmdList(args)
