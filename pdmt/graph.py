"""
A graph module written in python
"""
#import pydot

class Graph:
	def __init__(self):
		self.nodes=set()
		self.edges=dict()
		self.check=True
		self.check=False
	def check_have_node(self,node):
		if self.check:
			if node in self.nodes:
				raise ValueError("already have node",node)
	def check_havent_node(self,node):
		if self.check:
			if not node in self.nodes:
				raise ValueError("dont have node",node)
	""" assumes that fr and to are nodes """
	def check_havent_edge(self,fr,to):
		if self.check:
			if to in self.edges[fr]:
				raise ValueError("already have edge",fr,to)
	""" assumes that fr and to are nodes """
	def check_have_edge(self,fr,to):
		if self.check:
			if not to in self.edges[fr]:
				raise ValueError("dont have edge",fr,to)
	""" assumes that fr and to are nodes """
	def add_node(self,node):
		self.check_have_node(node)
		self.nodes.add(node)
		self.edges[node]=set()
	def remove_node(self,node):
		self.check_havent_node(node)
		self.nodes.remove(node)
		del self.edges[node]
	def add_edge(self,edge):
		(fr,to)=edge
		self.check_have_node(fr)
		self.check_have_node(to)
		self.check_havent_edge(fr,to)
		self.edges[fr].add(to)
	def remove_edge(self,edge):
		(fr,to)=edge
		self.check_have_node(fr)
		self.check_have_node(to)
		self.check_have_edge(fr,to)
		self.edges[fr].remove(to)
	def get_adjacent_for_node(self,node):
		for node in self.edges[node]:
			yield node
	def get_nodes(self):
		for node in self.nodes:
			yield node
	def get_edges(self):
		for fr in self.get_nodes():
			for to in self.get_adjacent_for_node(fr):
				yield (fr,to)
	def get_nodes_num(self):
		return len(self.nodes)
	""" depth first search algorithm """
	def dfs(self):
		visited=set()
		for node in self.get_nodes():
			if not node in visited:
				for v in self.dfs_unvisited_node(visited,node):
					yield v
	def dfs_unvisited_node(self,visited,v):
		if v in visited:
			return
		visited.add(v)
		for w in self.get_adjacent_for_node(v):
			for s in self.dfs_unvisited_node(visited,w):
				yield s
			if not w in visited:
				yield w
		yield v
	"""
	dump the graph in dot notation

	References:
	http://en.wikipedia.org/wiki/DOT_%28graph_description_language%29
	"""
	def print_dot(self):
		# header
		print('digraph pdmt {')
		id=1
		nodetoid={}
		for node in self.get_nodes():
			print(id,'[shape=box,label="'+str(node)+'"]',sep='')
			nodetoid[node]=id
			id+=1
		for (fr,to) in self.get_edges():
			print(nodetoid[fr],'->',nodetoid[to],';',sep='')
		print('}')

if __name__ == '__main__':
	g=Graph()
	g.add_node('a')
	g.add_node('b')
	for node in g.dfs():
		print(node)
