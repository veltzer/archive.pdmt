import pdmt.plugins.nodes.buildfile
import pdmt.plugins.nodes.cfile
import pdmt.utils.subproc
import pdmt.types

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	# new way of doing things
	#@staticmethod
	#def init(mgr):
	#	mgr.addTypedConfigDep('cfg://CCFLAGS')
	def __init__(self, name=None):
		super().__init__(name=name)
		self.add_edge(self.getConfigNode('CCFLAGS'))
	def filebuild(self):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.name)
		cfg_CCFLAGS=self.getConfig('CCFLAGS', '-O2')
		if cfg_CCFLAGS!='':
			args.append(cfg_CCFLAGS)
		# this assumes we have only a single source file
		args.append(self.getSourceOfType(pdmt.plugins.nodes.cfile.NodeType).name)
		pdmt.utils.subproc.check_call(args)
