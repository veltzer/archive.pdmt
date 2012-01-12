# the inheritance from 'object' is very important to get the __class__
# and other stuff we need in order for OO to work properly...
class Node(object):
	def __init__(self,p_type):
		self.m_type=p_type
	def setMgr(self,p_mgr):
		self.m_mgr=p_mgr
	def uptodate(self,todo):
		return True
	def canBuild(self):
		raise ValueError('must override')
	def build(self):
		raise ValueError('must override')
	def clean(self):
		pass
	def getDeps(self):
		return self.m_mgr.deps(self)
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
