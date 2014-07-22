'''
A build plan is what needs to be executed to make the build

TODO:
add a method call as a BuildPlanElement type.
'''

import pdmt.utils.subproc # for check_call
import pdmt.utils.printer # for print_msg_noeol_flush, print_msg, print_raw
import pdmt.utils.lang # for plural, book_to_ok

class BuildPlanElement(object):
	def execute():
		raise ValueError('must override')

class CmdList(BuildPlanElement):
	def __init__(self, arguments):
		super().__init__()
		self.arguments=arguments
	def execute(self):
		return pdmt.utils.subproc.system_list(self.arguments.args)
	def __str__(self):
		return ' '.join(self.arguments.args)

class CmdString(BuildPlanElement):
	def __init__(self, s):
		super().__init__()
		self.s=s
	def execute(self):
		return pdmt.utils.subproc.system_string(self.s)
	def __str__(self):
		return self.s

class Function(BuildPlanElement):
	def __init__(self, f):
		super().__init__()
		self.f=f
	def execute(self):
		self.f()
		return (0, '', '')
	def __str__(self):
		return self.f

'''
this is a build plan for a single node
'''
class NodeBuildPlan(object):
	def __init__(self, node):
		super().__init__()
		self.node=node
		self.list=[]
	def addCmdList(self, arguments):
		self.list.append(CmdList(arguments))
	def addCmdString(self, s):
		self.list.append(CmdString(s))
	def addFunction(self, f):
		self.list.append(Function(f))
	def execute(self):
		haveError=False
		self.node.last_err=0
		self.node.txt_out=''
		self.node.txt_err=''
		for l in self.list:
			(err, txt_out, txt_err)=l.execute()
			self.node.txt_out+=txt_out
			self.node.txt_err+=txt_err
			self.node.last_err=err
			if err:
				haveError=True
				break
		return haveError
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
		self.mgr=pdmt.mgr.Mgr.get_manager()
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
			pdmt.utils.printer.print_msg_noeol_flush('building ({num}/{len_list}) [{name}]...'.format(
				num=num+1,
				len_list=len_list,
				name=nbp.node.get_name(),
			))
			# FIXME - very simplistic approach
			ret=nbp.execute()
			s='['+pdmt.utils.lang.bool_to_ok(ret)+']'
			if nbp.node.txt_err!='' or nbp.node.txt_out!='':
				self.mgr.output_add(nbp.node)
				s+=' [OUTPUT]'
			else:
				self.mgr.output_remove(nbp.node)
			pdmt.utils.printer.print_raw(s)
			if ret:
				self.mgr.error_add(nbp.node)
				break
			else:
				self.mgr.error_remove(nbp.node)
	def print(self):
		for nbp in self.list:
			nbp.print()
