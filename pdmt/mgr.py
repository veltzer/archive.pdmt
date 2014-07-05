import pdmt.graph
import pdmt.config
import pdmt.cmdline
import pkgutil
import importlib
import inspect # for isclass
import pdmt.api

class Mgr:
	def __init__(self, loadinternalplugins=True):
		self.graph=pdmt.graph.Graph()
		self.init_handlers()
		self.opbyname={}
		if loadinternalplugins:
			self.loadInternalPlugins()

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
		return [node for node in self.graph.get_adjacent_for_node(node)]
	def depsYield(self,node):
		for n in self.graph.get_adjacent_for_node(node):
			yield n

	""" modification functions """
	def addNode(self,node):
		self.notify(node,'nodepreadd')
		self.graph.add_node(node)
		node.setMgr(self)
		self.notify(node,'nodepostadd')
	def delNode(self,node):
		self.notify(node,'nodepredel')
		self.graph.remove_node(node)
		node.setMgr(None)
		self.notify(node,'nodepostdel')
	def addEdge(self,edge):
		self.notify(edge,'edgepreadd')
		self.graph.add_edge(edge)
		self.notify(edge,'edgepostadd')
	def delEdge(self,edge):
		self.notify(edge,'edgepredel')
		self.graph.remove_edge(edge)
		self.notify(edge,'edgepostdel')
	def buildNode(self,node):
		self.notify(node,'nodeprebuild')
		node.build()
		self.notify(node,'nodepostbuild')

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
			self.buildNode(node)
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

	""" plugins """
	def addOperation(self,op):
		self.opbyname[op.getName()]=op
	def hasOperation(self,p_name):
		return p_name in self.opbyname
	def runOperation(self,p_name):
		#self.build()
		self.progress('running operation ['+p_name+']')
		op=self.opbyname[p_name]
		op.run()
	def getOperations(self):
		return self.opbyname

	""" printing methods """
	def printgraph(self):
		self.graph.print_dot();
	def dotgraph(self):
		self.graph.print_dot();

	""" helper functions to load all plugins """
	def loadPlugins(self, folder, namespace):
		for importer, modname, ispkg in pkgutil.walk_packages(
				path=[folder],
				prefix=namespace,
			):
			module=importlib.import_module(modname)
			for x in module.__dict__:
				curr=module.__dict__[x]
				if inspect.isclass(curr) and issubclass(curr, pdmt.api.Operation):
					m=curr()
					self.addOperation(m)
	def loadInternalPlugins(self):
		self.loadPlugins('pdmt/plugins/', 'pdmt.plugins.')

	""" command line parsing """
	def parseCmdline(self):
		pdmt.cmdline.parse(self)
