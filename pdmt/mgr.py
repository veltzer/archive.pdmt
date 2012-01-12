import pygraph.classes.digraph
#import pygraph.classes.graph
import pygraph.algorithms.searching

class Mgr:
	def __init__(self):
		self.graph=pygraph.classes.digraph.digraph()
		#self.graph=pygraph.classes.graph.graph()
		self.init_handlers()
		self.config={}
		#self.dbg=True
		self.dbg=False
		self.prog=True
		self.opnodes={}
		self.opbyname={}

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
			self.debug('examining ['+str(node)+']')
			if not node.uptodate(self,todo):
				todo.append(node)
		return todo
	def msg(self,message):
		print 'pdmt:',message
	def progress(self,message):
		if self.prog:
			self.msg(message)
	def debug(self,message):
		if self.dbg:
			self.msg(message)
	def build(self):
		todo=self.build_todolist()
		if len(todo)>0:
			name='node'
			if len(todo)>1:
				name+='s'
			self.progress('going to build '+str(len(todo))+' '+name)
		for num,node in enumerate(todo):
			self.progress('building ['+str(node)+']')
			node.build(self)
		if len(todo)==0:
			self.progress('nothing to build')
	def clean(self):
		lst=self.graph.nodes()
		if len(lst)>0:
			name='node'
			if len(lst)>1:
				name+='s'
		self.progress('going to clean '+str(len(lst))+' '+name)
		for node in self.graph.nodes():
			self.debug(node)
			node.clean()
	def dependsOn(self,nodes):
		ret=[]
		for node in nodes:
			for n in self.graph[node]:
				ret.append(n)
		return ret
	def addOperation(self,op,nodes):
		self.opbyname[op.getName()]=op
		self.opnodes[op]=nodes
	def runOperation(self,p_name):
		op=self.opbyname[p_name]
		nodes=self.opnodes[op]
		# TODO: build just the nodes we need, not all of them
		self.build()
		self.progress('running operation ['+p_name+']')
		op.run(nodes)
	""" print all operations """
	def dumpoperations(self):
		for x in self.opbyname:
			print x

	""" printing method """
	def dumpgraph(self):
		print self.graph
