import pdmt.plugins.nodes.operation # for NodeType
import pdmt.utils.lang # for plural
import pdmt.utils.subproc # for check_call

"""
A git cleaninng op
"""

class NodeType(pdmt.plugins.nodes.operation.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name='gitclean', proto=proto)
		self.description='very forceful git clean of a repository'
	def build(self):
		args=[]
		args.append('git')
		args.append('clean')
		args.append('-xdf')
		pdmt.utils.subproc.check_call(args)
