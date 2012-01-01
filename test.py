#!/usr/bin/python

import pdmt.mgr
import pdmt.nodehandlers.chandler
import pdmt.nodetypes.filenode
import pdmt.eventhandlers.debugger
import pygraph.algorithms.searching
#import mypygraph.searching

mgr=pdmt.mgr.Mgr()
mgr.addHandler(pdmt.nodehandlers.chandler.CHandler())
mgr.addHandler(pdmt.eventhandlers.debugger.Debugger())
node=pdmt.nodetypes.filenode.FileNode('tests/main.c')
mgr.addNode(node)
mgr.printme()
st, pre, post =pygraph.algorithms.searching.depth_first_search(mgr.graph)
print post
#for node in mypygraph.searching.depth_first_search_gen(mgr.graph): 
#	print node
