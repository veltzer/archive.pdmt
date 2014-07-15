import pdmt.plugins.nodes.operation # for NodeType
import pdmt.utils.lang # for plural
import pdmt.utils.subproc # for check_call

'''
A git cleaninng op
'''

class NodeType(pdmt.plugins.nodes.operation.NodeType):
	def __init__(self, **kw):
		super().__init__(name='gitclean', description='very forceful git clean of a repository', **kw)
	def build(self, nbp):
		args=[]
		args.append('git')
		args.append('clean')
		args.append('-xdf')
		nbp.addCmdList(args)
