import pdmt.plugins.nodes.build # for NodeType
import pdmt.plugins.nodes.file # for NodeType
import pdmt.utils.fileops # for unlinksoft

'''
	a mixin class representing a node that can be built (not source)
'''

class NodeType(pdmt.plugins.nodes.file.NodeType,pdmt.plugins.nodes.build.NodeType):
	def canClean(self):
		return True
	def clean(self):
		pdmt.utils.fileops.unlinksoft(self.name)
	def filebuild():
		raise ValueError('must override')
	def build(self):
		self.prebuild()
		self.filebuild()
		self.postbuild()
	''' maybe make sure to unlink the file before the build '''
	def prebuild(self):
		pass
	def postbuild(self):
		pdmt.utils.fileops.chmod(self.name,0o0444)
		pdmt.utils.fileops.checkexist_and_updatecache(self.name)
