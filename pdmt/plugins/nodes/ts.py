import pdmt.api # for NodeType
import dbm.gnu # for open
import time # for time

'''
This node is a node for which only a time stamp is stored
in a central managed db.
It is usually used as a time stamp node for collecting many nodes
together.
'''

def init():
	global dbm
	# 'c' means rw + create if needed
	dbm=dbm.gnu.open('.pdmt.gdbm', 'c')

def fini():
	global dbm
	dbm.close()

class NodeType(pdmt.api.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name=name, proto=proto)
		self.proto='ts'
	def get_lmt(self):
		return float(dbm[self.name])
	def canBuild(self):
		return True
	def build(self):
		global dbm
		dbm[self.name]=str(time.time())
	def clean(self):
		global dbm
		del dbm[self.name]


''' a method to debug this module '''
def print_all_entries():
	global dbm
	# show all key value pairs
	k=dbm.firstkey()
	while k is not None:
		print(k.decode(), dbm[k].decode())
		k=dbm.nextkey(k)
