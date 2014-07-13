import pdmt.api # for NodeType
import dbm.gnu # for open
import ast # for literal_eval
import time # for time

'''
This node is a node for which we have a time stamp and a value
in a central managed db.
It is usually used as a config node for plugins.
'''

def init():
	global dbm
	# 'c' means rw + create if needed
	dbm=dbm.gnu.open('.cfg.gdbm', 'c')

def fini():
	global dbm
	dbm.close()

class NodeType(pdmt.api.NodeType):
	def __init__(self, name=None):
		super().__init__(name=name, proto='cfg')
	def get_data(self):
		return ast.literal_eval(dbm[self.name].decode())
	def set_data(self, value):
		dbm[self.name]=str(value)
	def get_lmt(self):
		if self.name in dbm:
			return self.get_data()[0]
		else:
			return float(0)
	def get_value(self, default):
		if self.name in dbm:
			return self.get_data()[1]
		else:
			self.set_value(default)
			return default
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
	def clean(self):
		global dbm
		if self.name in dbm:
			del dbm[self.name]
	'''


''' a method to debug this module '''
def print_all_entries():
	global dbm
	# show all key value pairs
	k=dbm.firstkey()
	while k is not None:
		print(k.decode(), dbm[k].decode())
		k=dbm.nextkey(k)
