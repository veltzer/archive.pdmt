# the inheritance from 'object' is very important to get the __class__
# and other stuff we need in order for OO to work properly...
class Node(object):
	def __init__(self,p_type):
		self.m_type=p_type
	def uptodate(self,mgr,todo):
		return True
	def canBuild(self):
		raise ValueError('must override')
	def build(self,mgr):
		raise ValueError('must override')
	def clean(self):
		pass
