# the inheritance from 'object' is very important to get the __class__
# and other stuff we need in order for OO to work properly...
class NodeType(object):
	def __init__(self,p_type):
		self.m_type=p_type
	def setMgr(self,p_mgr):
		self.m_mgr=p_mgr
	def uptodate(self,todo):
		raise ValueError('must override')
	def canBuild(self):
		raise ValueError('must override')
	def build(self):
		raise ValueError('must override')
	def clean(self):
		raise ValueError('must override')
	def getDeps(self):
		return self.m_mgr.deps(self)
	def getDepsYield(self):
		for node in self.m_mgr.depsYield(self):
			yield node
	def getSourcesOfType(self,p_type):
		ret=[]
		for node in self.getDeps():
			if isinstance(node,p_type):
				ret.append(node)
		return ret
	def getSourceOfType(self,p_type):
		ret=self.getSourcesOfType(p_type)
		if len(ret)!=1:
			raise ValueError('too many sources')
		return ret[0]

"""
This is the base class of all operations within the system
"""
class Operation(object):
	def __init__(self,p_name,p_description):
		self.m_name=p_name
		self.m_description=p_description
	def getName(self):
		return self.m_name
	def getDescription(self):
		return self.m_description
	def run(self):
		raise ValueError('must override the operation')


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
