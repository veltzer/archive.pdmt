import pygraph.classes.digraph
import pygraph.algorithms.searching

class Mgr:
	def __init__(self):
		self.graph=pygraph.classes.digraph.digraph()
		self.init_handlers()
		self.config={}
		#self.debug=True
		self.debug=False
		self.progress=True

	""" listener functions start here """
	def init_handlers(self):
		self.handlers=set()
	def notify(self,data,eventtype):
		for h in self.handlers:
			h.respond(self,data,eventtype)
	def addHandler(self,handler):
		self.handlers.add(handler)
	def delHandler(self,handler):
		self.handlers.remove(handler)

	""" modification functions """
	def addNode(self,node):
		self.notify(node,'nodepreadd')
		self.graph.add_node(node)
		self.notify(node,'nodepostadd')
		return node
	def delNode(self,node):
		self.notify(node,'nodepredel')
		self.graph.remove_node(node)
		self.notify(node,'nodepostdel')
		return node
	def addEdge(self,edge):
		self.notify(edge,'edgepreadd')
		self.graph.add_edge(edge)
		self.notify(edge,'edgepostadd')
		return edge
	def delEdge(self,edge):
		self.notify(edge,'edgepredel')
		self.graph.remove_edge(edge)
		self.notify(edge,'edgepostdel')
		return edge

	""" configuration """
	def getConfig(self,name):
		return config[name]
	def setConfig(self,name,val):
		config[name]=val

	""" getting all dependencies for a node """
	def deps(self,node):
		for n in self.graph[node]:
			yield n

	""" building methods start here """

	""" this is a method that builds a list of all the nodes that need to be build.
	It build a real list. Maybe turn it into a generator ?
	"""
	def build_todolist(self):
		(st,pre,post)=pygraph.algorithms.searching.depth_first_search(self.graph)
		todo=[]
		for node in post:
			if self.debug:
				print 'examining',node
			if not node.uptodate(self):
				todo.append(node)
		return todo
	def build(self):
		todo=self.build_todolist()
		for node in todo:
			if self.progress:
				print 'building',node
			node.build(self)

	""" printing method """
	def printme(self):
		print self.graph
