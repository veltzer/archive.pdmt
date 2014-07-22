'''
A graph module written in python

This is the core graph module for pdmt.
Make sure it is efficient.

Properties:
- this graph is directed
- it holds edges in two directions (to answer reverse questions quickly)
'''
import pdmt.utils.string # for common_prefix
import pdmt.utils.printer # for print_raw
import sys # for getsizeof
import pdmt.event # for Event

class Graph(object):
	def __init__(self):
		self.nodes=set()
		self.edges=dict()
		self.edges_rv=dict()
		self.edges_num=0
		self.check=True
		#self.check=False
	''' memory size function '''
	def getsizeof(self):
		count=0
		count+=sys.getsizeof(self.nodes)
		for curr in self.nodes:
			count+=sys.getsizeof(curr)
		count+=sys.getsizeof(self.edges)
		for curr in self.edges:
			count+=sys.getsizeof(curr)
		count+=sys.getsizeof(self.edges_rv)
		for curr in self.edges_rv:
			count+=sys.getsizeof(curr)
		return count
	''' checking methods '''
	def check_have_node(self, node):
		if self.check:
			if not node in self.nodes:
				raise ValueError('already have node', node)
	def check_havent_node(self, node):
		if self.check:
			if node in self.nodes:
				raise ValueError('already have node', node)
	''' assumes that fr and to are nodes '''
	def check_havent_edge(self, fr, to):
		if self.check:
			if to in self.edges[fr]:
				raise ValueError('already have edge', fr, to)
	''' assumes that fr and to are nodes '''
	def check_have_edge(self, fr, to):
		if self.check:
			if not to in self.edges[fr]:
				raise ValueError('dont have edge', fr, to)
	''' assumes that fr and to are nodes '''
	def add_node(self, node):
		self.check_havent_node(node)
		self.nodes.add(node)
		self.edges[node]=set()
		self.edges_rv[node]=set()
	def remove_node(self, node):
		self.check_have_node(node)
		self.nodes.remove(node)
		del self.edges[node]
	def add_edge(self, edge):
		(fr, to)=edge
		self.check_have_node(fr)
		self.check_have_node(to)
		self.check_havent_edge(fr, to)
		self.edges[fr].add(to)
		self.edges_rv[to].add(fr)
		self.edges_num+=1
	def remove_edge(self, edge):
		(fr, to)=edge
		self.check_have_node(fr)
		self.check_have_node(to)
		self.check_have_edge(fr, to)
		self.edges[fr].remove(to)
		self.edges_rv[to].remove(fr)
		self.edges_num-=1
	def get_adjacent_for_node(self, node):
		for node in self.edges[node]:
			yield node
	'''
	The performance of this method is not critical since it is not
	used in the critical algorithms but only for debugging
	'''
	def get_rv_for_node(self, node):
		for node in self.edges_rv[node]:
			yield node
	def get_nodes(self):
		for node in self.nodes:
			yield node
	def get_edges(self):
		for fr in self.get_nodes():
			for to in self.get_adjacent_for_node(fr):
				yield (fr, to)
	def get_node_num(self):
		return len(self.nodes)
	def get_edge_num(self):
		return self.edges_num
	''' dependency for many nodes (not sure this works) '''
	def dependsOn(self, nodes):
		ret=[]
		for node in nodes:
			for n in self[node]:
				ret.append(n)
		return ret

'''
Typed graph. Graph that adds dependencies by type
'''
class TypedGraph(Graph):
	def __init__(self):
		super().__init__()
		self.typemap={}
		self.rv_typemap={}
	def addTypedConfigDep(self, cls, cfgname):
		node=self.get_node_by_name('cfg://'+cfgname)
		if cls not in self.typemap:
			self.typemap[cls]=[]
		if node not in self.rv_typemap:
			self.rv_typemap[node]=[]
		self.typemap[cls].append(node)
		self.rv_typemap[node].append(cls)
	def get_adjacent_for_node(self, node):
		yield from super().get_adjacent_for_node(node)
		if type(node) in self.typemap:
			for n in self.typemap[type(node)]:
				yield n
	def get_rv_for_node(self, node):
		yield from super().get_rv_for_node(node)
		for cls in self.rv_typemap[node]:
			for n in self.get_nodes():
				if type(n)==cls:
					yield n

'''
Some algorithms on the graph
'''
class AlgoGraph(TypedGraph):
	''' depth first search algorithm '''
	def dfs(self, node_list=None):
		visited=set()
		if node_list is None:
			node_list=self.get_nodes()
		for node in node_list:
			if not node in visited:
				for v in self.dfs_unvisited_node(visited, node):
					yield v
	def dfs_unvisited_node(self, visited, v):
		if v in visited:
			return
		visited.add(v)
		for w in self.get_adjacent_for_node(v):
			for s in self.dfs_unvisited_node(visited, w):
				yield s
			if not w in visited:
				yield w
		yield v

'''
This graph add names to the nodes. It assumes that each node has a name and holds a map
between names and nodes. nodes must not have the same name or you will get an exception
'''
class NamedGraph(AlgoGraph):
	def __init__(self):
		super().__init__()
		self.mymap={}
	def add_node(self, node):
		super().add_node(node)
		if node.get_name() in self.mymap:
			raise ValueError('already got', node.get_name())
		self.mymap[node.get_name()]=node
	def remove_node(self, node):
		del self.mymap[node.get_name()]
		super().remove_node(node)
	def has_name(self, name):
		return name in self.mymap
	def get_node_by_name(self, name):
		return self.mymap[name]

'''
This graph adds event handling being able to notify listeners when interesting stuff happens
to it
'''
debugEvents=False
class EventGraph(NamedGraph):
	def __init__(self):
		super().__init__()
		self.handlers=set()
	def notify(self, data=None, eventtype=None):
		for h in self.handlers:
			if debugEvents:
				print('dispatching', data, eventtype, 'to', h)
			h.respond(data=data, eventtype=eventtype)
	def addHandler(self, handler):
		self.handlers.add(handler)
	def delHandler(self, handler):
		self.handlers.remove(handler)

	''' modification functions '''
	def add_node(self, node):
		self.notify(data=node, eventtype=pdmt.event.Event.nodepreadd)
		super().add_node(node)
		self.notify(data=node, eventtype=pdmt.event.Event.nodepostadd)
	def remove_node(self, node):
		self.notify(data=node, eventtype=pdmt.event.Event.nodepredel)
		super().remove_node(node)
		self.notify(data=node, eventtype=pdmt.event.Event.nodepostdel)
	def add_edge(self, edge):
		self.notify(data=edge, eventtype=pdmt.event.Event.edgepreadd)
		super().add_edge(edge)
		self.notify(data=edge, eventtype=pdmt.event.Event.edgepostadd)
	def remove_edge(self, edge):
		self.notify(data=edge, eventtype=pdmt.event.Event.edgepredel)
		super().remove_edge(edge)
		self.notify(data=edge, eventtype=pdmt.event.Event.edgepostdel)

class PdmtGraph(EventGraph):
	'''
	dump the graph in dot notation

	References:
	http://en.wikipedia.org/wiki/DOT_%28graph_description_language%29
	'''
	def print_dot(self):
		# header
		print('digraph pdmt {')
		id=1
		nodetoid={}
		for node in self.get_nodes():
			print(id, '[shape=box, label="'+node.get_name()+'"]', sep='')
			nodetoid[node]=id
			id+=1
		for (fr, to) in self.get_edges():
			print(nodetoid[fr], '->', nodetoid[to], ';', sep='')
		print('}')
	def listnodes(self):
		l=[]
		for node in self.get_nodes():
			l.append(node.get_name())
		l.sort()
		for name in l:
			pdmt.utils.printer.print_raw(name)
	def listbuildnodes(self):
		l=[]
		for node in self.get_nodes():
			if node.canBuild():
				l.append(node.get_name())
		for name in sorted(l):
			pdmt.utils.printer.print_raw(name)
	def get_completions(self, prefix, canbuild, onlyName, filter_type):
		completions=[]
		for node in self.get_nodes():
			if filter_type is not None and not isinstance(node, filter_type):
				continue
			if onlyName:
				m=node.name
			else:
				m=node.get_name()
			if canbuild:
				c=node.canBuild()
			else:
				c=True
			if c and m.startswith(prefix):
				completions.append(m)
		return completions
	def bashcomplete(self, prefix):
		completions=self.get_completions(prefix, True, False, None)
		for completion in completions:
			print(completion)
	def bashcomplete_with_prefix(self, prefix):
		common=None
		l=[]
		for node in self.get_nodes():
			if node.canBuild() and node.get_name().startswith(prefix):
				if common is None:
					common=node.get_name()
				else:
					common=pdmt.utils.string.common_prefix(common, node.get_name())
				l.append(node.get_name())
				print(node.get_name())
		print(common)
		for x in l:
			print(x)

	''' make a list of nodes which are build nodes '''
	def get_build_node_list(self):
		retlist=[]
		for node in self.get_nodes():
			if node.canBuild():
				retlist.append(node)
		return retlist
	def get_build_node_list_sorted(self):
		retlist=self.get_build_node_list()
		retlist.sort(key=lambda x: x.get_name())
		return retlist
	''' make a list of nodes which are clean nodes '''
	def get_clean_node_list(self):
		retlist=[]
		for node in self.get_nodes():
			if node.canClean():
				retlist.append(node)
		return retlist
	def get_clean_node_list_sorted(self):
		retlist=self.get_clean_node_list()
		retlist.sort(key=lambda x: x.get_name())
		return retlist
