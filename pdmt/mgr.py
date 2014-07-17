import pdmt.graph # for PdmtGraph
import pdmt.config
import pdmt.cmdline
import pkgutil # for walk_packages
import importlib # for import_module
import inspect # for isclass
import pdmt.utils.lang # for plural
import pdmt.api # for Event.prebuild, Event.postbuild
import pdmt.exceptions # for CommandLineInputException
import types # for FunctionType
import pdmt.buildplan # for BuildPlan, NodeBuildPlan

class Mgr(pdmt.graph.PdmtGraph):
	def __init__(self, loadinternalplugins=True, cache=None):
		super().__init__()
		self.opbyname={}
		self.defaultNodeList=[]
		self.plugins=[]
		self.errors=set()
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

	''' getting all dependencies for a node '''
	def deps(self,node):
		return [node for node in self.get_adjacent_for_node(node)]
	def depsYield(self,node):
		for n in self.get_adjacent_for_node(node):
			yield n

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
		for node in self.dfs(node_list=node_list):
			self.debug('examining ['+str(node)+']')
			if node.needbuild(todo):
				todo.append(node)
		return todo
	def build_node_list(self, node_list):
		self.msg('going to scan [{len}] {plural}...'.format(
			len=len(node_list),
			plural=pdmt.utils.lang.plural('node', len(node_list)),
		))
		todo=self.build_todolist()
	def build_node_names(self, names):
		self.build(node_list=self.nodenames_to_nodes(names))
	def bp_node_names(self, names):
		return self.createPlan(node_list=self.nodenames_to_nodes(names))
	''' convert node names to nodes, throwing CommandLineInputException if not '''
	def nodenames_to_nodes(self, names):
		errors=[]
		ret=[]
		for name in names:
			if self.has_name(name):
				ret.append(self.get_node_by_name(name))
			else:
				errors.append('do not have node of name [{0}]'.format(name))
		if errors:
			raise pdmt.exceptions.CommandLineInputException(errors)
		return ret
	def createPlan(self, node_list=None):
		self.msg('going to scan [{len}] {plural}...'.format(
			len=self.get_node_num(),
			plural=pdmt.utils.lang.plural('node', self.get_node_num()),
		))
		if node_list is None:
			node_list=self.defaultNodeList
		todo=self.build_todolist(node_list)
		len_todo=len(todo)
		self.msg('creating a plan to build [{len_todo}] {plural}...'.format(
			len_todo=len_todo,
			plural=pdmt.utils.lang.plural('node', len_todo),
		))
		bp=pdmt.buildplan.BuildPlan(mgr=self)
		for num,node in enumerate(todo):
			self.progress('building plan for ({num}/{len_todo}) [{name}]'.format(
				num=num+1,
				len_todo=len_todo,
				name=node.get_name(),
			))
			nbp=pdmt.buildplan.NodeBuildPlan(node)
			node.build(nbp)
			bp.append(nbp)
		return bp
	def build(self, node_list=None):
		bp=self.createPlan(node_list)
		bp.execute()

	''' helper functions to load all plugins '''
	def loadPlugins(self, folder, namespace):
		for importer, modname, ispkg in pkgutil.walk_packages(
				path=[folder],
				prefix=namespace,
			):
			module=importlib.import_module(modname)
			if 'init' in module.__dict__ and type(module.init) is types.FunctionType:
				module.init(self)
			# search for classes that have initializers
			for name,t in module.__dict__.items():
				# is it a new type
				if type(t) is type:
					if 'init' in t.__dict__ and type(t.init) is types.FunctionType:
						t.init(self)
			self.plugins.append(module)
	def loadInternalPlugins(self):
		self.loadPlugins('pdmt/plugins/', 'pdmt.plugins.')

	''' command line parsing '''
	def parseCmdline(self):
		pdmt.cmdline.parse(self)

	'''shutdown method to clean up, currently does nothing'''
	def shutdown(self):
		for module in reversed(self.plugins):
			if 'fini' in module.__dict__ and type(module.fini) is types.FunctionType:
				module.fini(self)

	'''error handling code'''
	def error_add(self, node):
		self.errors.add(node)
	def error_remove(self, node):
		if node in self.errors:
			self.errors.remove(node)

	def getConfigNode(self, name):
		nodename='cfg://'+name
		if self.has_name(nodename):
			return self.get_node_by_name(nodename)
		else:
			return pdmt.plugins.nodes.cfg.NodeType(name=name, mgr=self)
