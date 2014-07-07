import pdmt.api # for NodeHandler
import re # for compile

"""
This is a node connector. It listens for 'nodepostadd' events
and connects nodes that match a regualr expression to the node
given to it at construction.

TODO: It should also listen for the removal of the node given to it
and remove itself when it is removed.
"""
class NodeHandler(pdmt.api.NodeHandler):
	def __init__(self,cnode,typefilter,regexp):
		self.cnode=cnode
		self.typefilter=typefilter
		self.regexp=re.compile(regexp)
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		#print('t2 connecting ',self.cnode.get_name())
		if not isinstance(node,self.typefilter):
			return
		#print('t1 connecting ',self.cnode.get_name(), node.get_name())
		if not self.regexp.match(node.name):
			return
		#print('connecting ',self.cnode.get_name(), node.get_name())
		mgr.addEdge((self.cnode,node))
