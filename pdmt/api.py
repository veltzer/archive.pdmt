# the inheritance from 'object' is very important to get the __class__
# and other stuff we need in order for OO to work properly...
class NodeType(object):
	def __init__(self, type=None, name=None, description=None, proto=None):
		super().__init__()
		if type is None:
			self.type='unset'
		else:
			self.type=type
		if proto is None:
			self.proto='node'
		else:
			self.proto=proto
		if name is None:
			self.name='unset'
		else:
			self.name=name
		if description is None:
			self.description='unset'
		else:
			self.description=description
	def get_name(self):
		return '{proto}/{name}'.format(
			proto=self.proto,
			name=self.name
		)
	def setMgr(self,mgr):
		self.mgr=mgr
	def uptodate(self,todo):
		raise ValueError('must override')
	def canBuild(self):
		raise ValueError('must override')
	def build(self):
		raise ValueError('must override')
	def clean(self):
		raise ValueError('must override')
	def getDeps(self):
		return self.mgr.deps(self)
	def getDepsYield(self):
		for node in self.mgr.depsYield(self):
			yield node
	def getSourcesOfType(self,type):
		ret=[]
		for node in self.getDeps():
			if isinstance(node,type):
				ret.append(node)
		return ret
	def getSourceOfType(self,type):
		ret=self.getSourcesOfType(type)
		if len(ret)!=1:
			raise ValueError('too many sources')
		return ret[0]

"""
This is the base class of all operations within the system
"""
class Operation(object):
	def __init__(self,p_name,p_description):
		self.name=p_name
		self.description=p_description
	def getName(self):
		return self.name
	def getDescription(self):
		return self.description
	def run(self):
		raise ValueError('must override')


"""
This is the base class of all node handlers within the system
"""

class NodeHandler(object):
	def respond(self,mgr,node,eventtype):
		raise ValueError('must override')


"""
This is the base class of all event handlers within the system
"""

class EventHandler(object):
	def respond(self,pdmt,data,eventtype):
		raise ValueError('must override')

"""
This is the cache handler
"""
class Cache(object):
	def has_checksum(self, checksum):
		raise ValueError('must override')
	def get_filename(self, checksum, filename):
		raise ValueError('must override')
	def put_filename(self, checksum, filename):
		raise ValueError('must override')
