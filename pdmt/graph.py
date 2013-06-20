"""
A graph module written in python
"""

from __future__ import print_function

class Graph:
	def __init__(self):
		self.nodes=set()
		self.edges=dict()
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
	def get_deps_for(self,node):
		for node in self.edges[node]:
			yield node
	def get_nodes(self):
		for node in self.nodes:
			yield node
	def get_nodes_num(self):
		return len(self.nodes)
