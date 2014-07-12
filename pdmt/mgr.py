import pdmt.graph # for PdmtGraph
import pdmt.config
import pdmt.cmdline
import pkgutil # for walk_packages
import importlib # for import_module
import inspect # for isclass
import pdmt.utils.lang # for plural
import pdmt.api # for Event.prebuild, Event.postbuild
import pdmt.exceptions # for CommandLineInputException

class Mgr:
	def __init__(self, loadinternalplugins=True, cache=None):
		self.graph=pdmt.graph.PdmtGraph()
		self.init_handlers()
		self.opbyname={}
		self.defaultNodeList=[]
		self.plugins=[]
		if loadinternalplugins:
			self.loadInternalPlugins()
		#if cache is None:
		#	self.cache=pdmt.plugins.cache.null.NullCache()
		#else:
		#	self.cache=cache

	def setDefaultNodeList(self, nodelist):
		self.defaultNodeList=nodelist

	''' cache methods '''
	def get_cache(self):
		return self.cache
	def set_cache(self, cache):
		self.cache=cache

	''' listener functions start here '''
	def init_handlers(self):
		self.handlers=set()
	def notify(self,data,eventtype):
		for h in self.handlers:
			h.respond(self,data,eventtype)
	def addHandler(self,handler):
		self.handlers.add(handler)
	def delHandler(self,handler):
		self.handlers.remove(handler)

	''' getting all dependencies for a node '''
	def deps(self,node):
		return [node for node in self.graph.get_adjacent_for_node(node)]
	def depsYield(self,node):
		for n in self.graph.get_adjacent_for_node(node):
			yield n

	''' modification functions '''
	def addNode(self,node):
		self.notify(node, pdmt.api.Event.nodepreadd)
		self.graph.add_node(node)
		node.setMgr(self)
		self.notify(node, pdmt.api.Event.nodepostadd)
	def delNode(self,node):
		self.notify(node, pdmt.api.Event.nodepredel)
		self.graph.remove_node(node)
		node.setMgr(None)
		self.notify(node, pdmt.api.Event.nodepostdel)
	def addEdge(self,edge):
		self.notify(edge, pdmt.api.Event.edgepreadd)
		self.graph.add_edge(edge)
		self.notify(edge, pdmt.api.Event.edgepostadd)
	def delEdge(self,edge):
		self.notify(edge, pdmt.api.Event.edgepredel)
		self.graph.remove_edge(edge)
		self.notify(edge, pdmt.api.Event.edgepostdel)

	''' debugging methods '''

	def msg(self,message):
		print('pdmt:',message)
	def progress(self,message):
		if pdmt.config.ns_mgr.p_prog:
			self.msg(message)
	def debug(self,message):
		if pdmt.config.ns_mgr.p_dbg:
			self.msg(message)

	''' building methods start here '''

	'''
	this is a method that builds a list of all the nodes that need to be build.
	It builds a real list. Maybe turn it into a generator ?
	The fact that it builds a list is bad since a list is ok for serial building
	but not for parallel.
	references:
	http://en.wikipedia.org/wiki/Topological_sorting
	'''
	def build_todolist(self, node_list):
		todo=[]
		for node in self.graph.dfs(node_list=node_list):
			self.debug('examining ['+str(node)+']')
			if node.needbuild(todo):
				todo.append(node)
		return todo
	def buildNode(self,node):
		self.notify(node, pdmt.api.Event.nodeprebuild)
		node.build()
		self.notify(node, pdmt.api.Event.nodepostbuild)
	def build_node_list(self, node_list):
		self.progress('going to scan [{len}] {plural}...'.format(
			len=len(node_list),
			plural=pdmt.utils.lang.plural('node', len(node_list)),
		))
		todo=self.build_todolist()
	def verify_node_names(self, names, doexit):
		errors=[]
		for name in names:
			if not self.graph.has_name(name):
				errors.append('do not have node of name [{0}]'.format(name))
		if errors and doexit:
			raise pdmt.exceptions.CommandLineInputException(errors)
		else:
			return errors
	def build_node_names(self, names):
		self.build((self.graph.get_node_by_name(name) for name in names))
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

	''' helper functions to load all plugins '''
	def loadPlugins(self, folder, namespace):
		for importer, modname, ispkg in pkgutil.walk_packages(
				path=[folder],
				prefix=namespace,
			):
			module=importlib.import_module(modname)
			if 'init' in module.__dict__:
				module.init()
			self.plugins.append(module)
	def loadInternalPlugins(self):
		self.loadPlugins('pdmt/plugins/', 'pdmt.plugins.')

	''' command line parsing '''
	def parseCmdline(self):
		pdmt.cmdline.parse(self)

	'''shutdown method to clean up, currently does nothing'''
	def shutdown(self):
		for module in reversed(self.plugins):
			if 'fini' in module.__dict__:
				module.fini()
