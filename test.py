#!/usr/bin/python

import pdmt.mgr
import pdmt.nodehandlers.chandler
import pdmt.nodehandlers.debugger
import pdmt.nodetypes.filenode
import pdmt.edgehandlers.debugger

mgr=pdmt.mgr.Mgr()
mgr.addNodeHandler(pdmt.nodehandlers.chandler.CHandler())
#mgr.addNodeHandler(pdmt.nodehandlers.debugger.Debugger())
#mgr.addEdgeHandler(pdmt.edgehandlers.debugger.Debugger())
node=pdmt.nodetypes.filenode.FileNode('tests/main.c')
mgr.addNode(node)
mgr.printme()
