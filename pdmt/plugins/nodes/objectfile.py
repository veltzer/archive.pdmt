import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.cfile # for NodeType

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	# new way of doing things
	#@staticmethod
	#def init(mgr):
	#	mgr.addTypedConfigDep('cfg://CCFLAGS')
	def __init__(self, **kw):
		super().__init__(**kw)
		self.add_edge(self.getConfigNode('CCFLAGS'))
	def filebuild(self, nbp):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.name)
		cfg_CCFLAGS=self.getConfig('CCFLAGS')
		if cfg_CCFLAGS!='':
			args.append(cfg_CCFLAGS)
		# this assumes we have only a single source file
		args.append(self.getSourceOfType(pdmt.plugins.nodes.cfile.NodeType).name)
		nbp.addCmdList(args)
