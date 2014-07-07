import pdmt.graph
import pdmt.config
import pdmt.cmdline
import pkgutil # for walk_packages
import importlib # for import_module
import inspect # for isclass
import pdmt.utils.lang # for plural

class Mgr:
	def __init__(self, loadinternalplugins=True, cache=None):
		self.graph=pdmt.graph.Graph()
		self.init_handlers()
		self.opbyname={}
		if loadinternalplugins:
			self.loadInternalPlugins()
		#if cache is None:
		#	self.cache=pdmt.plugins.cache.null.NullCache()
		#else:
		#	self.cache=cache

	""" cache methods """
	def get_cache(self):
		return self.cache
	def set_cache(self, cache):
		self.cache=cache

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
			self.progress('going to build '+str(len(todo))+' '+pdmt.utils.lang.plural('node', len(todo)))
			for num,node in enumerate(todo):
				self.progress('building ['+str(node)+']')
				self.buildNode(node)
		else:
			self.progress('nothing to build')
	def dependsOn(self,nodes):
		ret=[]
		for node in nodes:
			for n in self.graph[node]:
				ret.append(n)
		return ret

	""" printing methods """
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
	def loadInternalPlugins(self):
		self.loadPlugins('pdmt/plugins/', 'pdmt.plugins.')

	""" command line parsing """
	def parseCmdline(self):
		pdmt.cmdline.parse(self)
