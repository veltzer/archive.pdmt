import pdmt.nodetypes.objectfilenode
import re

"""
This is a node connector. It listens for 'nodepostadd' events
and connects nodes that match a regualr expression to the node
given to it at construction.

TODO: It should also listen for the removal of the node given to it
and remove itself when it is removed.
"""
class Connector:
	def __init__(self,cnode,typefilter,regexp):
		self.cnode=cnode
		self.typefilter=typefilter
		self.regexp=re.compile(regexp)
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,self.typefilter):
			return
		if not self.regexp.match(node.m_fname):
			return
		mgr.addEdge((self.cnode,node))
