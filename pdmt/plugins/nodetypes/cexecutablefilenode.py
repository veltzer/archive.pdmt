import pdmt.plugins.nodetypes.buildfilenode
import pdmt.plugins.nodetypes.objectfilenode
import pdmt.utils.subproc
import pdmt.types

class NodeType(pdmt.plugins.nodetypes.buildfilenode.NodeType):
	def __init__(self,p_fname):
		super().__init__(p_fname,pdmt.types.t_exe)
	def build(self):
		args=[]
		args.append('gcc')
		args.append('-o')
		args.append(self.m_fname)
		for node in self.getSourcesOfType(pdmt.plugins.nodetypes.objectfilenode.NodeType):
			args.append(node.m_fname)
		pdmt.utils.subproc.check_call(args)
