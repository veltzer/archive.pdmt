#!/usr/bin/python3

import pdmt.mgr
import glob # for glob

mgr=pdmt.mgr.Mgr()
mgr.loadAllOps()
mgr.loadAllTypes()
mgr.loadAllHandlers()
mgr.loadAllEventHandlers()

# debugging
mgr.addHandler(pdmt.eventhandlers.debugger.EventHandler())
mgr.addHandler(pdmt.nodehandlers.dirmaker.NodeHandler())

# c stuff
mgr.addHandler(pdmt.nodehandlers.chandler.NodeHandler())
node=mgr.addNode(pdmt.nodetypes.cexecutablefilenode.NodeType('tests/main.exe'))
mgr.addHandler(pdmt.nodehandlers.connector.NodeHandler(node,pdmt.nodetypes.objectfilenode.NodeType,'^tests/.*\.o$'))
mgr.addNode(pdmt.nodetypes.cfilenode.NodeType('tests/main.c'))

# mako stuff
mgr.addHandler(pdmt.nodehandlers.makohandler.NodeHandler())
for name in glob.glob('mako/*.mako'):
	mgr.addNode(pdmt.nodetypes.makofilenode.NodeType(name))

mgr.parseCmdline()
