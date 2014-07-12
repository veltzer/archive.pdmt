import cmd # for Cmd
import os # for system
import pdmt.config # for ns_pdmt

'''
references:
http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/cmd/index.html
'''

class Pdmt(cmd.Cmd):
	def __init__(self, mgr):
		super().__init__()
		self.mgr=mgr
		self.prompt='pdmt> '
	def postcmd(self, stop, line):
		return stop
	def no_args(self, cmd, arg):
		if arg!='':
			print('command [{0}] does not take any arguments'.format(cmd))
			return True
		else:
			return False
	def help_stats(self):
		print('show stats for the current graph')
	def do_stats(self, arg):
		if self.no_args('stats', arg):
			return
		print('graph has [{0}] nodes'.format(
			self.mgr.graph.get_node_num(),
		))
		print('graph has [{0}] edges'.format(
			self.mgr.graph.get_edge_num(),
		))
	def complete_build(self, text, line, begidx, endidx):
		last_arg=line.split()[-1]
		if last_arg=='build':
			last_arg=''
		completions=self.mgr.graph.get_completions(last_arg)
		return [c[len(last_arg)-len(text):] for c in completions]
	def help_build(self):
		print('build [nodes]: build nodes')
	def do_build(self, arg):
		names=arg.split()
		errors=self.mgr.verify_node_names(names, False)
		if errors:
			for error in errors:
				print(error)
		else:
			self.mgr.build_node_names(names)
	def help_exit(self):
		print('exit pdmt shell')
	def do_exit(self, arg):
		return True
	help_EOF=help_exit
	def do_EOF(self, arg):
		print()
		return True
	def help_shell(self):
		print('run a shell command')
	def do_shell(self, arg):
		os.system(arg)

def go(mgr):
	ins=Pdmt(mgr)
	banner='Welcome to pdmt [{0}]...'.format(
		pdmt.config.ns_pdmt.p_version,
	)
	ins.cmdloop(banner)
