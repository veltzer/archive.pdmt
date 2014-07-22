import pdmt.api # for NodeType
import dbm.gnu # for open
import ast # for literal_eval
import time # for time
import os.path # for isfile

'''
This node is a node for which we have a time stamp and a value
in a central managed db.
It is usually used as a config node for plugins.
'''

handle=None
def init(mgr):
	global handle
	filename='.cfg.gdbm'
	haveFile=os.path.isfile(filename)
	# 'c' means rw + create if needed
	handle=dbm.gnu.open(filename, 'c')
	# put defaults inside
	if not haveFile:
		set_val('CC', 'gcc')
		set_val('CCFLAGS', '-O2')
		set_val('LD', 'gcc')
		set_val('LDFLAGS', '')
	# add all nodes to the graph
	k=handle.firstkey()
	while k is not None:
		(key, value)=(k.decode(), handle[k].decode())
		NodeType(name=key)
		k=handle.nextkey(k)

def set_val(name, value):
	global handle
	tup=(time.time(), value)
	handle[name]=str(tup)

def get_val(name):
	global handle
	return ast.literal_eval(handle[name].decode())

def fini(mgr):
	global handle
	handle.close()

class NodeType(pdmt.api.NodeType):
	def __init__(self, **kw):
		super().__init__(proto='cfg', **kw)
		(self.lmt, self.value)=get_val(self.name)
	'''
	def get_data(self):
		return get_val(self.name)
	def set_data(self, value):
		set_value(self.name, value)
	def get_lmt(self):
		return self.get_data()[0]
	def get_value(self):
		return self.get_data()[1]
	'''
	def get_lmt(self):
		return self.lmt
	def get_value(self):
		return self.value
	def set_value(self, value):
		self.value=value
		set_val(self.name, self.value)
		self.lmt=time.time()
	def canBuild(self):
		return False
	# we don't really want to clean cfg nodes for now...
	def canClean(self):
		return False
		#return True
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
