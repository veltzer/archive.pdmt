import pdmt.api
import pdmt.utils.subproc

"""
A git cleaninng op
"""

class Operation(pdmt.api.Operation):
	def __init__(self):
		super().__init__(
			'gitclean',
			'very forceful git clean of a repository',
		)
	def run(self):
		args=[]
		args.append('git')
		args.append('clean')
		args.append('-xdf')
		pdmt.utils.subproc.check_call(args)
