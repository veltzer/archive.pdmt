#!/usr/bin/python3

"""
Test suite for pdmt.

Documentation for unittest for python3 is here:
https://docs.python.org/3/library/unittest.html
"""

import unittest # for TestCase
import pdmt.graph # for Graph
import pdmt.stack # for Stack
import pdmt.utils.subproc # for system_pipe

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		pass
	def test_graph(self):
		g=pdmt.graph.Graph()
		g.add_node('a')
		g.add_node('b')
		count=0
		for node in g.dfs():
			count+=1
		self.assertEqual(count,2)
	def test_stack(self):
		s=pdmt.stack.Stack()
		s.push(3)
		s.push(4)
		s.push(5)
		l=[]
		for x in s.foreach():
			l.append(x)
		self.assertEqual(l, [3,4,5])
		self.assertEqual(5, s.pop());
		self.assertEqual(4, s.pop());
		self.assertEqual(3, s.pop());
	@unittest.skip("subproc testing disabled for now")
	def test_subproc(self):
		try:
			# test error in first command
			pdmt.utils.subproc.system_pipe(
				['ls','-l','/etc/passwd'],
				['wc','-l'],
			);
		except ValueError as e:
			print('ok, got error for first command',e)
		try:
			# test error in second command
			pdmt.utils.subproc.system_pipe(
				['ls','-l'],
				['wc','-l','--stam'],
			);
		except ValueError as e:
			print('ok, got error for second command',e)
		# test output
		pdmt.utils.subproc.system_pipe(
			['ls','-l'],
			['wc','-l'],
			out=open('/dev/null','w'),
		);

unittest.main()
