#!/usr/bin/python3

import pdmt.mgr
import pdmt.cmdline
import glob # for glob
import os # for environ

mgr=pdmt.mgr.Mgr()
mgr.loadAllOps()
mgr.loadAllTypes()
mgr.loadAllHandlers()
mgr.loadAllEventHandlers()

if os.environ.get("PDMT_DEBUG") != None:
	mgr.addHandler(pdmt.eventhandlers.debugger.EventHandler())

# c stuff
mgr.addHandler(pdmt.nodehandlers.chandler.NodeHandler())
node=mgr.addNode(pdmt.nodetypes.cexecutablefilenode.NodeType('tests/main.exe'))
mgr.addHandler(pdmt.nodehandlers.connector.NodeHandler(node,pdmt.nodetypes.objectfilenode.NodeType,'^tests/.*\.o$'))
mgr.addNode(pdmt.nodetypes.cfilenode.NodeType('tests/main.c'))

# mako stuff
mgr.addHandler(pdmt.nodehandlers.makohandler.NodeHandler())
nodes=[]
for name in glob.glob('mako/*.mako'):
	nodes.append(mgr.addNode(pdmt.nodetypes.makofilenode.NodeType(name)))

pdmt.cmdline.parse(mgr)
