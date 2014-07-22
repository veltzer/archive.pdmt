import cmd # for Cmd
import os # for system
import pdmt.config # for ns_pdmt
import pdmt.utils.printer # for print_msg
import pdmt.mgr # for Mgr
import sys # for argv

'''
references:
http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/cmd/index.html
'''

class Pdmt(cmd.Cmd):
	def __init__(self):
		super().__init__()
		self.mgr=pdmt.mgr.Mgr.get_manager()
		self.prompt='pdmt> '

	'''
	HELPER METHODS
	'''

	''' all prints should go through this method '''
	def print_msg(self, msg):
		pdmt.utils.printer.print_msg(msg)
	''' special print function for special situations when you don't
	want anything special added '''
	def print_raw(self, msg, **kw):
		print(msg, **kw)
	''' print errors '''
	def error(self, msg):
		pdmt.utils.printer.print_msg(msg)

	def postcmd(self, stop, line):
		return stop
	def no_args(self, cmd, arg):
		if arg!='':
			self.print_msg('command [{0}] does not take any arguments'.format(cmd))
			return True
		else:
			return False
	def check_args(self, arg, num):
		return len(arg.split())==num
	def build_one_node(self, name):
		if self.mgr.has_name(name):
			self.mgr.build_node_names([name])
		else:
			self.print_msg('for clean to work please defined a node [{name}]...'.format(name=name))
	def complete_nodes(self, text, line, begidx, endidx, canbuild, onlyName, filter_type):
		parts=line.split()
		if len(parts)==1:
			last_arg=''
		else:
			last_arg=parts[-1]
		completions=self.mgr.get_completions(last_arg, canbuild, onlyName, filter_type)
		return [c[len(last_arg)-len(text):] for c in completions]

	'''
	COMMANDS
	'''
	def help_listplugins(self):
		self.print_msg('show all plugins')
	def do_listplugins(self, arg):
		if self.no_args('listplugins', arg):
			return
		self.mgr.listPlugins()

	def help_listnodetypes(self):
		self.print_msg('show all nodetypes')
	def do_listnodetypes(self, arg):
		if self.no_args('listnodetypes', arg):
			return
		self.mgr.listNodetypes()

	def help_liststaticdeps(self):
		self.print_msg('show all static dependencies')
	def do_liststaticdeps(self, arg):
		if self.no_args('liststaticdeps', arg):
			return
		self.mgr.liststaticdeps()

	def help_listbuildnodes(self):
		self.print_msg('show all build nodes in the current graph')
	def do_listbuildnodes(self, arg):
		if self.no_args('listbuildnodes', arg):
			return
		self.mgr.listbuildnodes()

	def help_listnodes(self):
		self.print_msg('show all nodes in the current graph')
	def do_listnodes(self, arg):
		if self.no_args('listnodes', arg):
			return
		self.mgr.listnodes()

	def help_listall(self):
		self.print_msg('show the current graph')
	def do_listall(self, arg):
		if self.no_args('listall', arg):
			return
		for node in self.mgr.get_nodes():
			self.print_raw(node.get_name())
			for an in self.mgr.get_adjacent_for_node(node):
				self.print_raw('\t'+an.get_name())

	def complete_cfgget(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, False, True, pdmt.plugins.nodes.cfg.NodeType)
	def help_cfgget(self):
		self.print_msg('get config values')
	def do_cfgget(self, arg):
		if not self.check_args(arg, 1):
			self.error('please supply a cfg name')
			return
		name=arg.split()[0].strip()
		nodename='cfg://'+name
		if not self.mgr.has_name(nodename):
			self.error('do not have config named [{0}]'.format(name))
			return
		node=self.mgr.get_node_by_name(nodename)
		self.print_raw(node.get_value(None))

	def complete_cfgset(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, False, True, pdmt.plugins.nodes.cfg.NodeType)
	def help_cfgset(self):
		self.print_msg('set config values')
	def do_cfgset(self, arg):
		if not self.check_args(arg, 2):
			self.error('please supply a cfg name and a value')
			return
		name=arg.split()[0].strip()
		value=arg.split()[1].strip()
		# handle empty values
		if value[0]=='"' and value[-1]=='"':
			value=value[1:-1]
		self.mgr.getConfigNode(name).set_value(value)

	def help_stats(self):
		self.print_msg('show stats for the current graph')
	def do_stats(self, arg):
		if self.no_args('stats', arg):
			return
		self.print_msg('graph has [{0}] nodes'.format(
			self.mgr.get_node_num(),
		))
		self.print_msg('graph has [{0}] edges'.format(
			self.mgr.get_edge_num(),
		))

	def help_ts_print_all_entries(self):
		self.print_msg('print all time stamp entries')
	def do_ts_print_all_entries(self, arg):
		if self.no_args('ts_print_all_entries', arg):
			return
		pdmt.plugins.nodes.ts.print_all_entries()

	def help_cfgshow(self):
		self.print_msg('print all cfg entries')
	def do_cfgshow(self, arg):
		if self.no_args('cfg_print_all_entries', arg):
			return
		pdmt.plugins.nodes.cfg.print_all_entries()

	def help_getsizeof(self):
		self.print_msg('print the size that the graph takes in bytes')
	def do_getsizeof(self, arg):
		if self.no_args('getsizeof', arg):
			return
		self.print_msg('getsizeof is [{0}]'.format(self.mgr.getsizeof()))

	def help_clean(self):
		self.print_msg('clean everything')
	def do_clean(self, arg):
		if self.no_args('clean', arg):
			return
		self.build_one_node('phony://clean')

	def help_errors(self):
		self.print_msg('show nodes in errors')
	def do_errors(self, arg):
		if self.no_args('errors', arg):
			return
		for node in self.mgr.errors:
			self.print_raw(node.get_name())

	def help_showoutputs(self):
		self.print_msg('show outputs of outputed nodes')
	def do_showoutputs(self, arg):
		if self.no_args('showoutputs', arg):
			return
		for node in self.mgr.nodes_outputs:
			self.print_raw(node.get_name())
			self.print_raw('================ STDERR ==================')
			self.print_raw(node.txt_err, end='')
			self.print_raw('================ STDOUT ==================')
			self.print_raw(node.txt_out, end='')
			self.print_raw('==========================================')

	def help_showerrors(self):
		self.print_msg('show errors of errored nodes')
	def do_showerrors(self, arg):
		if self.no_args('showerrors', arg):
			return
		for node in self.mgr.nodes_errors:
			self.print_raw(node.get_name())
			self.print_raw('================ STDERR ==================')
			if node.txt_err[-1]=='\n':
				self.print_raw(node.txt_err, end='')
			else:
				self.print_raw(node.txt_err)
			self.print_raw('================ STDOUT ==================')
			if node.txt_out[-1]=='\n':
				self.print_raw(node.txt_out, end='')
			else:
				self.print_raw(node.txt_out)
			self.print_raw('==========================================')
			self.print_raw(str(node.last_err))

	def help_build(self):
		self.print_msg('build the default target')
	def do_build(self, arg):
		if self.no_args('build', arg):
			return
		self.build_one_node('phony://all')

	def help_plan(self):
		self.print_msg('show plan to build the default target')
	def do_plan(self, arg):
		if self.no_args('plan', arg):
			return
		self.mgr.createPlan().print()

	def complete_buildnodes(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, True, False, None)
	def help_buildnodes(self):
		self.print_msg('buildnodes [nodes]: build nodes by specific names')
	def do_buildnodes(self, arg):
		names=arg.split()
		try:
			self.mgr.build_node_names(arg.split())
		except pdmt.exceptions.CommandLineInputException as e:
			e.print()

	def complete_depends(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, True, False, None)
	def help_depends(self):
		self.print_msg('depends [nodes]: show what do nodes depend on (1 level)')
	def do_depends(self, arg):
		try:
			for node in self.mgr.nodenames_to_nodes(arg.split()):
				self.print_raw(node.get_name())
				for an in self.mgr.get_adjacent_for_node(node):
					self.print_raw('\t'+an.get_name())
		except pdmt.exceptions.CommandLineInputException as e:
			e.print()

	def complete_whatdependson(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, False, False, None)
	def help_whatdependson(self):
		self.print_msg('whatdependson [nodes]: show what nodes depend on nodes (1 level)')
	def do_whatdependson(self, arg):
		names=arg.split()
		try:
			for node in self.mgr.nodenames_to_nodes(arg.split()):
				self.print_raw(node.get_name())
				for an in self.mgr.get_rv_for_node(node):
					self.print_raw('\t'+an.get_name())
		except pdmt.exceptions.CommandLineInputException as e:
			e.print()

	def help_exit(self):
		self.print_msg('exit pdmt shell')
	def do_exit(self, arg):
		return True

	def help_EOF(self):
		self.print_msg('exit pdmt shell')
	def do_EOF(self, arg):
		self.print_raw('')
		return True

	def help_shell(self):
		self.print_msg('run a shell command')
	def do_shell(self, arg):
		os.system(arg)

	def help_playground(self):
		self.print_msg('developer playground')
	def do_playground(self, arg):
		import os
		e = os.popen('stty size', 'r').read().split()
		print(e)
		#import console
		#e = console.getTerminalSize()
		#print(e)

def go():
	ins=Pdmt()
	banner='Welcome to pdmt [{0}]...'.format(
		pdmt.config.ns_pdmt.p_version,
	)
	ins.print_msg(banner)
	ins.cmdloop()
