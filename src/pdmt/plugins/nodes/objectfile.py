import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.cfile # for NodeType

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	@classmethod
	def init(cls, mgr):
		mgr.addTypedConfigDep(cls, 'CC')
		mgr.addTypedConfigDep(cls, 'CCFLAGS')
	def filebuild(self, nbp):
		args=self.createArgs()
		args.appendConfig('CC')
		args.append('-c')
		args.append('-o')
		args.append(self.name)
		args.appendConfigIfNotEmpty('CCFLAGS')
		# this assumes we have only a single source file
		args.append(self.getSourceOfType(pdmt.plugins.nodes.cfile.NodeType).name)
		nbp.addCmdList(args)
