#!/usr/bin/python

import pdmt.mgr
import pdmt.nodehandlers.chandler
import pdmt.nodetypes.filenode
#import pdmt.eventhandlers.debugger
import mypygraph.searching

mgr=pdmt.mgr.Mgr()
mgr.addNodeHandler(pdmt.nodehandlers.chandler.CHandler())
#mgr.addEventHandler(pdmt.eventhandlers.debugger.Debugger())
node=pdmt.nodetypes.filenode.FileNode('tests/main.c')
mgr.addNode(node)
#mgr.printme()
for node in mypygraph.searching.depth_first_search_gen(mgr.graph): 
	print node
