import cmd # for Cmd
import os # for system
import pdmt.config # for ns_pdmt

class Pdmt(cmd.Cmd):
	def __init__(self, mgr):
		super().__init__()
		self.mgr=mgr
		self.prompt='pdmt> '
	def postcmd(self, stop, line):
		return stop
	def do_stats(self, arg):
		print('graph has [{0}] nodes...'.format(
			self.mgr.graph.get_node_num(),
		))
	def do_exit(self, arg):
		return True
	def do_EOF(self, arg):
		print()
		return True
	def do_shell(self, arg):
		os.system(arg)

def go(mgr):
	ins=Pdmt(mgr)
	banner='Welcome to pdmt [{0}]...'.format(
		pdmt.config.ns_pdmt.p_version,
	)
	ins.cmdloop(banner)
