import pdmt.graph # for NamedGraph
import pdmt.config
import pdmt.cmdline
import pkgutil # for walk_packages
import importlib # for import_module
import inspect # for isclass
import pdmt.utils.lang # for plural

class Mgr:
	def __init__(self, loadinternalplugins=True, cache=None):
		self.graph=pdmt.graph.NamedGraph()
		self.init_handlers()
		self.opbyname={}
		self.defaultNodeList=[]
		if loadinternalplugins:
			self.loadInternalPlugins()
		#if cache is None:
		#	self.cache=pdmt.plugins.cache.null.NullCache()
		#else:
		#	self.cache=cache

	def setDefaultNodeList(self, nodelist):
		self.defaultNodeList=nodelist

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

	""" debugging methods """

	def msg(self,message):
		print('pdmt:',message)
	def progress(self,message):
		if pdmt.config.ns_mgr.p_prog:
			self.msg(message)
	def debug(self,message):
		if pdmt.config.ns_mgr.p_dbg:
			self.msg(message)

	""" building methods start here """

	"""
	this is a method that builds a list of all the nodes that need to be build.
	It builds a real list. Maybe turn it into a generator ?
	The fact that it builds a list is bad since a list is ok for serial building
	but not for parallel.
	references:
	http://en.wikipedia.org/wiki/Topological_sorting
	"""
	def build_todolist(self, node_list):
		todo=[]
		for node in self.graph.dfs(node_list=node_list):
			self.debug('examining ['+str(node)+']')
			if not node.uptodate(todo):
				todo.append(node)
		return todo
	def buildNode(self,node):
		self.notify(node,'nodeprebuild')
		node.build()
		self.notify(node,'nodepostbuild')
	def build_node_list(self, node_list):
		self.progress('going to scan [{len}] {plural}...'.format(
			len=len(node_list),
			plural=pdmt.utils.lang.plural('node', len(node_list)),
		))
		todo=self.build_todolist()
	def build_node_names(self, names):
		node_list=[]
		for name in names:
			if self.graph.has_name(name):
				node_list.append(self.graph.get_node_by_name(name))
			else:
				raise ValueError('do not have node of name', name)
		self.build(node_list)
	def build(self, node_list=None):
		self.progress('going to scan [{len}] {plural}...'.format(
			len=self.graph.get_node_num(),
			plural=pdmt.utils.lang.plural('node', self.graph.get_node_num()),
		))
		if node_list is None:
			node_list=self.defaultNodeList
		todo=self.build_todolist(node_list)
		len_todo=len(todo)
		self.progress('going to build [{len_todo}] {plural}...'.format(
			len_todo=len_todo,
			plural=pdmt.utils.lang.plural('node', len_todo),
		))
		for num,node in enumerate(todo):
			self.progress('building ({num}/{len_todo}) [{name}]'.format(
				num=num+1,
				len_todo=len_todo,
				name=node.get_name(),
			))
			self.buildNode(node)

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
