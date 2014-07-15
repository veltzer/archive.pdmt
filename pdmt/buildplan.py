'''
A build plan is what needs to be executed to make the build

TODO:
add a method call as a BuildPlanElement type.
'''

import pdmt.utils.subproc # for check_call
import pdmt.utils.printer # for print_msg
import pdmt.utils.lang # for plural

class BuildPlanElement(object):
	def execute():
		raise ValueError('must override')

class CmdList(BuildPlanElement):
	def __init__(self, l):
		super().__init__()
		self.l=l
	def execute(self):
		pdmt.utils.subproc.check_call(self.l)
	def __str__(self):
		return ' '.join(self.l)

class CmdString(BuildPlanElement):
	def __init__(self, s):
		super().__init__()
		self.s=s
	def execute(self):
		pdmt.utils.subproc.check_call(self.s)

class Function(BuildPlanElement):
	def __init__(self, f):
		super().__init__()
		self.f=f
	def execute(self):
		self.f()

'''
this is a build plan for a single node
'''
class NodeBuildPlan(object):
	def __init__(self, node):
		super().__init__()
		self.node=node
		self.list=[]
	def addCmdList(self, l):
		self.list.append(CmdList(l))
	def addFunction(self, f):
		self.list.append(Function(f))
	def execute(self):
		for l in self.list:
			l.execute()
	def print(self):
		print(self.node.get_name())
		for l in self.list:
			print('\t'+str(l))

'''
this is a build plan for many nodes. It has the nodes and for each the
build plan.

Currently it is just a list of NodeBuildPlan
'''
class BuildPlan(object):
	def __init__(self):
		super().__init__()
		self.list=[]
	def append(self, nbp):
		self.list.append(nbp)
	def execute(self):
		len_list=len(self.list)
		pdmt.utils.printer.print_msg('executing build of [{len_list}] {plural}...'.format(
			len_list=len_list,
			plural=pdmt.utils.lang.plural('node', len_list),
		))
		for num, nbp in enumerate(self.list):
			pdmt.utils.printer.print_msg('building ({num}/{len_list}) [{name}]'.format(
				num=num+1,
				len_list=len_list,
				name=nbp.node.get_name(),
			))
			nbp.execute()
	def print(self):
		for nbp in self.list:
			nbp.print()
