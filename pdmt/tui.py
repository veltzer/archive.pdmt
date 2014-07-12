import cmd2 # for Cmd
import os # for system
import pdmt.config # for ns_pdmt
import pdmt.utils.printer # for print_msg
import sys # for argv

'''
references:
http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/cmd/index.html
'''

class Pdmt(cmd2.Cmd):
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
	def postcmd(self, stop, line):
		return stop
	def no_args(self, cmd, arg):
		if arg!='':
			self.print('command [{0}] does not take any arguments'.format(cmd))
			return True
		else:
			return False
	def help_listnodes(self):
		self.print('show all nodes in the current graph')
	def do_listnodes(self, arg):
		if self.no_args('stats', arg):
			return
		self.mgr.graph.listnodes()
	def help_stats(self):
		self.print('show stats for the current graph')
	def do_stats(self, arg):
		if self.no_args('stats', arg):
			return
		self.print('graph has [{0}] nodes'.format(
			self.mgr.graph.get_node_num(),
		))
		self.print('graph has [{0}] edges'.format(
			self.mgr.graph.get_edge_num(),
		))
	def help_tsall(self):
		self.print('print all time stamp entries')
	def do_tsall(self, arg):
		if self.no_args('stats', arg):
			return
		pdmt.plugins.nodes.ts.print_all_entries()
	def help_clean(self):
		self.print('clean everything')
	def do_clean(self, arg):
		if self.no_args('stats', arg):
			return
		self.mgr.build_node_names(['op://clean'])
	def help_build(self):
		self.print('build the default target')
	def do_build(self, arg):
		if self.no_args('stats', arg):
			return
		self.mgr.build()
	def complete_nodes(self, text, line, begidx, endidx, canbuild):
		parts=line.split()
		if len(parts)==1:
			last_arg=''
		else:
			last_arg=parts[-1]
		completions=self.mgr.graph.get_completions(last_arg, canbuild)
		return [c[len(last_arg)-len(text):] for c in completions]
	def complete_buildnodes(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, True)
	def help_buildnodes(self):
		self.print('buildnodes [nodes]: build nodes by specific names')
	def do_buildnodes(self, arg):
		names=arg.split()
		errors=self.mgr.verify_node_names(names, False)
		if errors:
			for error in errors:
				self.print(error)
		else:
			self.mgr.build_node_names(names)
	complete_depends=complete_buildnodes
	def help_depends(self):
		self.print('depends [nodes]: show what do nodes depend on (1 level)')
	def do_depends(self, arg):
		names=arg.split()
		errors=self.mgr.verify_node_names(names, False)
		if errors:
			for error in errors:
				self.print(error)
		else:
			for name in names:
				node=self.mgr.graph.get_node_by_name(name)
				self.raw_print(node.get_name())
				for an in self.mgr.graph.get_adjacent_for_node(node):
					self.raw_print('\t'+an.get_name())
	def complete_whatdependson(self, text, line, begidx, endidx):
		return self.complete_nodes(text, line, begidx, endidx, False)
	def help_whatdependson(self):
		self.print('whatdependson [nodes]: show what nodes depend on nodes (1 level)')
	def do_whatdependson(self, arg):
		names=arg.split()
		errors=self.mgr.verify_node_names(names, False)
		if errors:
			for error in errors:
				self.print(error)
		else:
			for name in names:
				node=self.mgr.graph.get_node_by_name(name)
				self.raw_print(node.get_name())
				for an in self.mgr.graph.get_rv_for_node(node):
					self.raw_print('\t'+an.get_name())
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
	sys.argv.remove('--tui')
	ins=Pdmt(mgr)
	banner='Welcome to pdmt [{0}]...'.format(
		pdmt.config.ns_pdmt.p_version,
	)
	ins.print(banner)
	ins.cmdloop()
