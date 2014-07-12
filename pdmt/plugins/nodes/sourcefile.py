import pdmt.plugins.nodes.file # for NodeType
import os.path # for isfile

'''
this node represents an source file. Not just C. Any source file
'''

class NodeType(pdmt.plugins.nodes.file.NodeType):
	''' if a source file exists then it is upto date '''
	''' question: why isn't a source file ALWAYS up to date?
	answer: what if the source file went missing? We want to trigger
	an error. Well - is it this methods part to check that the file
	exists ?!? I don't think so. This methods name is called *needbuild*
	and not *verify* or something... '''
	def needbuild(self,todo):
		return False
#		return not os.path.isfile(self.name)
	def canBuild(self):
		return False
	def clean(self):
		pass
	''' maybe we can checkout the source files...:) ?!? '''
	def build(self):
		raise ValueError('dont know how to build a source file')
