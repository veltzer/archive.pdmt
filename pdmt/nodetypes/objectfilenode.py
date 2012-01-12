import buildfilenode
import cfilenode
import pdmt.utils.subproc
import pdmt.types

class ObjectFileNode(buildfilenode.BuildFileNode):
	def __init__(self,p_fname):
		super(ObjectFileNode,self).__init__(p_fname,pdmt.types.t_object)
	def build(self):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.m_fname)
		for node in self.getSourcesOfType(cfilenode.CFileNode):
			args.append(node.m_fname)
		pdmt.utils.subproc.check_call(args)
