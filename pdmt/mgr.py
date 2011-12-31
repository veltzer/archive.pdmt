import pygraph.classes.digraph

class Mgr:
	def __init__(self):
		self.graph=pygraph.classes.digraph.digraph()
		self.nodeHandlers=set()
		self.edgeHandlers=set()

	""" node handling functions start here """
	def notifyNode(self,node,eventtype):
		for h in self.nodeHandlers:
			h.respond(self,node,eventtype)
	def addNodeHandler(self,handler):
		self.nodeHandlers.add(handler)
	def delNodeHandler(self,handler):
		self.nodeHandlers.remove(handler)
	def addNode(self,node):
		self.notifyNode(node,'preadd')
		self.graph.add_node(node)
		self.notifyNode(node,'postadd')
		return node
	def delNode(self,node):
		self.notifyNode(node,'predel')
		self.graph.remove_node(node)
		self.notifyNode(node,'postdel')
		return node

	""" edge handling functions start here """
	def notifyEdge(self,edge,eventtype):
		for h in self.edgeHandlers:
			h.respond(self,edge,eventtype)
	def addEdgeHandler(self,handler):
		self.edgeHandlers.add(handler)
	def delEdgeHandler(self,handler):
		self.edgeHandlers.remove(handler)
	def addEdge(self,edge):
		self.notifyEdge(edge,'preadd')
		self.graph.add_edge(edge)
		self.notifyEdge(edge,'postadd')
		return edge
	def delEdge(self,edge):
		self.notifyEdge(edge,'predel')
		self.graph.remove_edge(edge)
		self.notifyEdge(edge,'postdel')
		return edge

	""" building methods start here """
	def build(self):
		pass

	""" printing method """
	def printme(self):
		print self.graph
