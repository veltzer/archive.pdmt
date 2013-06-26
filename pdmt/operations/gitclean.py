import pdmt.operations.operation
import pdmt.utils.subproc

"""
A git cleaninng op
"""

class GitClean(pdmt.operations.operation.Operation):
	def __init__(self):
		pdmt.operations.operation.Operation.__init__(
			self,
			"gitclean",
			"very forceful git clean of a repository",
		)
	def run(self,nodes):
		args=[]
		args.append('git');
		args.append('clean');
		args.append('-xdf');
		pdmt.utils.subproc.check_call(args)
