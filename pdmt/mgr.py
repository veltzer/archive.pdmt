import pdmt.graph
import pdmt.config

class Mgr:
	def __init__(self):
		#self.graph=pygraph.classes.digraph.digraph()
		#self.graph=pygraph.classes.graph.graph()
		self.graph=pdmt.graph.Graph()
		self.init_handlers()
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

	""" getting all dependencies for a node """
	def deps(self,node):
		for n in self.graph.get_adjacent_for_node(node):
			yield n

	""" modification functions """
	def addNode(self,node):
		self.notify(node,'nodepreadd')
		self.graph.add_node(node)
		node.setMgr(self)
		self.notify(node,'nodepostadd')
		return node
	def delNode(self,node):
		self.notify(node,'nodepredel')
		self.graph.remove_node(node)
		node.setMgr(None)
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

	""" building methods start here """

	""" this is a method that builds a list of all the nodes that need to be build.
	It build a real list. Maybe turn it into a generator ?
	"""
	def build_todolist(self):
		todo=[]
		for node in self.graph.dfs():
			self.debug('examining ['+str(node)+']')
			if not node.uptodate(todo):
				todo.append(node)
		return todo
	def msg(self,message):
		print('pdmt:',message)
	def progress(self,message):
		if pdmt.config.ns_mgr.p_prog:
			self.msg(message)
	def debug(self,message):
		if pdmt.config.ns_mgr.p_dbg:
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
			node.build()
		if len(todo)==0:
			self.progress('nothing to build')
	def clean(self):
		lst_len=self.graph.get_nodes_num()
		if lst_len>0:
			name='node'
			if lst_len>1:
				name+='s'
		self.progress('going to clean '+str(lst_len)+' '+name)
		for node in self.graph.get_nodes():
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
	def hasOperation(self,p_name):
		return p_name in self.opbyname
	def runOperation(self,p_name):
		op=self.opbyname[p_name]
		nodes=self.opnodes[op]
		# TODO: build just the nodes we need, not all of them
		self.build()
		self.progress('running operation ['+p_name+']')
		op.run(nodes)
	def getOperations(self):
		return self.opbyname

	""" printing method """
	def printgraph(self):
		self.graph.print_dot();
	def dotgraph(self):
		self.graph.print_dot();
		"""
		dot=pygraph.readwrite.dot.write(self.graph)
		f=open('/tmp/graph.dot','w')
		f.write(dot)
		f.close()
		"""
		#gvv=gv.readstring(dot)
		#gv.layout(gvv,'dot')
		#gv.render(gvv,'png','/tmp/graph.png')
		#gv.render(gvv,'svg','/tmp/graph.svg')
		#gv.render(gvv,'svg','/tmp/graph.svg')
