#!/usr/bin/python

import pdmt.mgr
import pdmt.nodehandlers.chandler
import pdmt.nodetypes.sourcefilenode
import pdmt.eventhandlers.debugger

debug=False

mgr=pdmt.mgr.Mgr()
mgr.addHandler(pdmt.nodehandlers.chandler.CHandler())
if debug:
	mgr.addHandler(pdmt.eventhandlers.debugger.Debugger())
node=pdmt.nodetypes.sourcefilenode.SourceFileNode('tests/main.c')
mgr.addNode(node)
if debug:
	mgr.printme()
mgr.build()
