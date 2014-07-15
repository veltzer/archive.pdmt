import pdmt.api # for NodeType
import dbm.gnu # for open
import ast # for literal_eval
import time # for time

'''
This node is a node for which we have a time stamp and a value
in a central managed db.
It is usually used as a config node for plugins.
'''

handle=None
def init(mgr):
	global handle
	# 'c' means rw + create if needed
	handle=dbm.gnu.open('.cfg.gdbm', 'c')

def fini(mgr):
	global handle
	handle.close()

class NodeType(pdmt.api.NodeType):
	def __init__(self, **kw):
		super().__init__(proto='cfg', **kw)
	def get_data(self):
		global handle
		return ast.literal_eval(handle[self.name].decode())
	def set_data(self, value):
		global handle
		handle[self.name]=str(value)
	def get_lmt(self):
		if self.name in handle:
			return self.get_data()[0]
		else:
			return float(0)
	def get_value(self):
		return self.get_data()[1]
	def set_value(self, value):
		tup=(time.time(), value)
		self.set_data(tup)
	def canBuild(self):
		return False
	def canClean(self):
		return False
		#return True
	# we don't really want to clean cfg nodes for now...
	'''
	def clean(self, nbp):
		def dowork():
			global handle
			if self.name in handle:
				del handle[self.name]
		nbp.addFunction(nbp)
	'''


''' a method to debug this module '''
def print_all_entries():
	global handle
	# show all key value pairs
	k=handle.firstkey()
	while k is not None:
		print(k.decode(), handle[k].decode())
		k=handle.nextkey(k)
