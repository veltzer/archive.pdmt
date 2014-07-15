import cmd # for Cmd
import os # for system
import pdmt.config # for ns_pdmt
import pdmt.utils.printer # for print_msg
import sys # for argv

'''
references:
http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/cmd/index.html
'''

class Pdmt(cmd.Cmd):
	def __init__(self, mgr):
		super().__init__()
		self.mgr=mgr
		self.prompt='pdmt> '

	''' all prints should go through this method '''
	def print(self, msg):
		pdmt.utils.printer.print_msg(msg)
	''' special print function for special situations when you don't
	want anything special added '''
	def raw_print(self, msg):
		print(msg)
	''' print errors '''
	def error(self, msg):
		pdmt.utils.printer.print_msg(msg)

	def postcmd(self, stop, line):
		return stop
	def no_args(self, cmd, arg):
		if arg!='':
			self.print('command [{0}] does not take any arguments'.format(cmd))
			return True
		else:
			return False
	def check_args(self, arg, num):
		return len(arg.split())==num
	def help_listbuildnodes(self):
		self.print('show all build nodes in the current graph')
	def do_listbuildnodes(self, arg):
		if self.no_args('listbuildnodes', arg):
			return
		self.mgr.listbuildnodes()
	def help_listnodes(self):
		self.print('show all nodes in the current graph')
	def do_listnodes(self, arg):
		if self.no_args('listnodes', arg):
			return
		self.mgr.listnodes()
	def help_listall(self):
		self.print('show the current graph')
	def do_listall(self, arg):
		if self.no_args('listall', arg):
			return
		for node in self.mgr.get_nodes():
			self.raw_print(node.get_name())
			for an in self.mgr.get_adjacent_for_node(node):
				self.raw_print('\t'+an.get_name())
	def complete_getcfg(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, False, True, pdmt.plugins.nodes.cfg.NodeType)
	def help_getcfg(self):
		self.print('get config values')
	def do_getcfg(self, arg):
		if not self.check_args(arg, 1):
			self.error('please supply a cfg name')
			return
		name=arg.split()[0].strip()
		nodename='cfg://'+name
		if not self.mgr.has_name(nodename):
			self.error('do not have config named [{0}]'.format(name))
			return
		node=self.mgr.get_node_by_name(nodename)
		self.raw_print(node.get_value(None))
	def complete_setcfg(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, False, True, pdmt.plugins.nodes.cfg.NodeType)
	def help_setcfg(self):
		self.print('set config values')
	def do_setcfg(self, arg):
		if not self.check_args(arg, 2):
			self.error('please supply a cfg name and a value')
			return
		name=arg.split()[0].strip()
		value=arg.split()[1].strip()
		if value[0]=='"' and value[-1]=='"':
			value=value[1:-1]
		nodename='cfg://'+name
		if not self.mgr.has_name(nodename):
			self.error('do not have config named [{0}]'.format(name))
			return
		node=self.mgr.get_node_by_name(nodename)
		node.set_value(value)
	def help_stats(self):
		self.print('show stats for the current graph')
	def do_stats(self, arg):
		if self.no_args('stats', arg):
			return
		self.print('graph has [{0}] nodes'.format(
			self.mgr.get_node_num(),
		))
		self.print('graph has [{0}] edges'.format(
			self.mgr.get_edge_num(),
		))
	def help_ts_print_all_entries(self):
		self.print('print all time stamp entries')
	def do_ts_print_all_entries(self, arg):
		if self.no_args('ts_print_all_entries', arg):
			return
		pdmt.plugins.nodes.ts.print_all_entries()
	def help_cfg_print_all_entries(self):
		self.print('print all cfg entries')
	def do_cfg_print_all_entries(self, arg):
		if self.no_args('cfg_print_all_entries', arg):
			return
		pdmt.plugins.nodes.cfg.print_all_entries()
	def help_getsizeof(self):
		self.print('print the size that the graph takes in bytes')
	def do_getsizeof(self, arg):
		if self.no_args('getsizeof', arg):
			return
		self.print('getsizeof is [{0}]'.format(self.mgr.getsizeof()))
	def help_clean(self):
		self.print('clean everything')
	def do_clean(self, arg):
		if self.no_args('clean', arg):
			return
		self.mgr.build_node_names(['op://clean'])
	def help_errors(self):
		self.print('show nodes in errors')
	def do_errors(self, arg):
		if self.no_args('errors', arg):
			return
		for node in self.mgr.errors:
			print(node.get_name())
	def help_showerrors(self):
		self.print('show errors errored nodes')
	def do_showerrors(self, arg):
		if self.no_args('showerrors', arg):
			return
		for node in self.mgr.errors:
			print(node.get_name())
			print('\t'+node.txt_err)
			print('\t'+node.txt_out)
			print('\t'+str(node.last_err))
	def help_build(self):
		self.print('build the default target')
	def do_build(self, arg):
		if self.no_args('build', arg):
			return
		self.mgr.build()
	def help_plan(self):
		self.print('show plan to build the default target')
	def do_plan(self, arg):
		if self.no_args('plan', arg):
			return
		self.mgr.createPlan().print()
	def complete_nodes(self, text, line, begidx, endidx, canbuild, onlyName, filter_type):
		parts=line.split()
		if len(parts)==1:
			last_arg=''
		else:
			last_arg=parts[-1]
		completions=self.mgr.get_completions(last_arg, canbuild, onlyName, filter_type)
		return [c[len(last_arg)-len(text):] for c in completions]
	def complete_buildnodes(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, True, False, None)
	def help_buildnodes(self):
		self.print('buildnodes [nodes]: build nodes by specific names')
	def do_buildnodes(self, arg):
		names=arg.split()
		try:
			self.mgr.build_node_names(arg.split())
		except pdmt.exceptions.CommandLineInputException as e:
			e.print()
	complete_depends=complete_buildnodes
	def help_depends(self):
		self.print('depends [nodes]: show what do nodes depend on (1 level)')
	def do_depends(self, arg):
		try:
			for node in self.mgr.nodenames_to_nodes(arg.split()):
				self.raw_print(node.get_name())
				for an in self.mgr.get_adjacent_for_node(node):
					self.raw_print('\t'+an.get_name())
		except pdmt.exceptions.CommandLineInputException as e:
			e.print()
	def complete_whatdependson(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, False, False, None)
	def help_whatdependson(self):
		self.print('whatdependson [nodes]: show what nodes depend on nodes (1 level)')
	def do_whatdependson(self, arg):
		names=arg.split()
		try:
			for node in self.mgr.nodenames_to_nodes(arg.split()):
				self.raw_print(node.get_name())
				for an in self.mgr.get_rv_for_node(node):
					self.raw_print('\t'+an.get_name())
		except pdmt.exceptions.CommandLineInputException as e:
			e.print()
	def help_exit(self):
		self.print('exit pdmt shell')
	def do_exit(self, arg):
		return True
	help_EOF=help_exit
	def do_EOF(self, arg):
		self.raw_print('')
		return True
	def help_shell(self):
		self.print('run a shell command')
	def do_shell(self, arg):
		os.system(arg)

def go(mgr):
	#sys.argv.remove('--tui')
	ins=Pdmt(mgr)
	banner='Welcome to pdmt [{0}]...'.format(
		pdmt.config.ns_pdmt.p_version,
	)
	ins.print(banner)
	ins.cmdloop()
