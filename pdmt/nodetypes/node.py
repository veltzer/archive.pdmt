class Node:
	def uptodate(self,mgr):
		return True
	def canBuild(self):
		raise ValueError('must override')
	def build(self,mgr):
		raise ValueError('must override')
