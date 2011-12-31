import pygraph.classes.digraph

class Mgr:
	def __init__(self):
		self.graph=pygraph.classes.digraph.digraph()
		self.nodeHandlers=set()
		self.edgeHandlers=set()
		self.config={}

	""" node handling functions start here """
	def notifyNode(self,node,eventtype):
		for h in self.nodeHandlers:
			h.respond(self,node,eventtype)
	def addNodeHandler(self,handler):
		self.nodeHandlers.add(handler)
	def delNodeHandler(self,handler):
		self.nodeHandlers.remove(handler)
	def addNode(self,node):
		self.notifyNode(node,'nodepreadd')
		self.graph.add_node(node)
		self.notifyNode(node,'nodepostadd')
		return node
	def delNode(self,node):
		self.notifyNode(node,'nodepredel')
		self.graph.remove_node(node)
		self.notifyNode(node,'nodepostdel')
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
		self.notifyEdge(edge,'edgepreadd')
		self.graph.add_edge(edge)
		self.notifyEdge(edge,'edgepostadd')
		return edge
	def delEdge(self,edge):
		self.notifyEdge(edge,'edgepredel')
		self.graph.remove_edge(edge)
		self.notifyEdge(edge,'edgepostdel')
		return edge

	""" general event handlers """
	def addEventHandler(self,handler):
		self.nodeHandlers.add(handler)
		self.edgeHandlers.add(handler)
	def delEventHandler(self,handler):
		self.nodeHandlers.remove(handler)
		self.edgeHandlers.remove(handler)
	
	""" configuration """
	def getConfig(self,name):
		return config[name]
	def setConfig(self,name,val):
		config[name]=val

	""" building methods start here """
	def build(self):
		nodes=self.graph

	""" printing method """
	def printme(self):
		print self.graph
