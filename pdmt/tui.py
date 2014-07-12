import cmd # for Cmd

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

def go(mgr):
	ins=Pdmt(mgr)
	banner='welcome to pdmt...'
	#print(dir(ins))
	ins.cmdloop(banner)
