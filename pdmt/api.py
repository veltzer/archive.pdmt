import enum # for Enum
import pdmt.prl # for create
import pdmt.mgr # for Mgr

# the inheritance from 'object' is very important to get the __class__
# and other stuff we need in order for OO to work properly...
class NodeType(object):
	def __init__(self, type=None, name=None, description=None, proto=None, mgr=None):
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
		if mgr is None:
			self.mgr=pdmt.mgr.Mgr.default
		else:
			self.mgr=mgr
		self.mgr.graph.add_node(self)
	def get_name(self):
		return pdmt.prl.create(
			proto=self.proto,
			name=self.name
		)
	def needbuild(self,todo):
		# lets compare dates
		rebuild=False
		for node in self.getDeps():
			if node in todo:
				rebuild=True
				break
			if node.get_lmt()>self.get_lmt():
				rebuild=True
				break
		return rebuild
	def canBuild(self):
		raise ValueError('must override')
	def build(self):
		raise ValueError('must override')
	def canClean(self):
		raise ValueError('must override')
	def clean(self):
		raise ValueError('must override')
	def get_lmt(self):
		return float(0)
	def getDeps(self):
		return self.mgr.deps(self)
	def getDepsYield(self):
		for node in self.mgr.depsYield(self):
			yield node
	def getSourcesOfType(self, type):
		ret=[]
		for node in self.getDeps():
			if isinstance(node,type):
				ret.append(node)
		return ret
	def getSourceOfType(self, type):
		ret=self.getSourcesOfType(type)
		if len(ret)!=1:
			raise ValueError('too many sources')
		return ret[0]
	def getConfigNode(self, name):
		nodename='cfg://'+name
		if self.mgr.graph.has_name(nodename):
			return self.mgr.graph.get_node_by_name(nodename)
		else:
			return pdmt.plugins.nodes.cfg.NodeType(name=name)
	def getConfig(self, name, default):
		return self.mgr.graph.get_node_by_name('cfg://'+name).get_value(default)
	def add_edge(self, node):
		self.mgr.graph.add_edge((self, node))

'''
This is the base class of all node handlers within the system
'''

class NodeHandler(object):
	def __init__(self, mgr=None):
		if mgr is None:
			self.mgr=pdmt.mgr.Mgr.default
		else:
			self.mgr=mgr
	def respond(self,data=None,eventtype=None):
		raise ValueError('must override')


'''
This is the base class of all event handlers within the system
'''

class EventHandler(object):
	def __init__(self, mgr=None):
		if mgr is None:
			self.mgr=pdmt.mgr.Mgr.default
		else:
			self.mgr=mgr
	def respond(self,data=None,eventtype=None):
		raise ValueError('must override')

'''
This is the cache handler
'''

class Cache(object):
	def has_checksum(self, checksum):
		raise ValueError('must override')
	def get_filename(self, checksum, filename):
		raise ValueError('must override')
	def put_filename(self, checksum, filename):
		raise ValueError('must override')

'''
These are events which a user of the core can register
to
'''
class Event(enum.Enum):
	nodepreadd=1
	nodepostadd=2
	nodepredel=3
	nodepostdel=4
	edgepreadd=5
	edgepostadd=6
	edgepredel=7
	edgepostdel=8
	nodeprebuild=9
	nodepostbuild=10
