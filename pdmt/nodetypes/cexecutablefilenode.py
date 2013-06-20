import pdmt.nodetypes.buildfilenode
import pdmt.nodetypes.objectfilenode
import pdmt.utils.subproc
import pdmt.types

class CExecutableFileNode(pdmt.nodetypes.buildfilenode.BuildFileNode):
	def __init__(self,p_fname):
		super(CExecutableFileNode,self).__init__(p_fname,pdmt.types.t_exe)
	def build(self):
		args=[]
		args.append('gcc')
		args.append('-o')
		args.append(self.m_fname)
		for node in self.getSourcesOfType(objectfilenode.ObjectFileNode):
			args.append(node.m_fname)
		pdmt.utils.subproc.check_call(args)
