#!/usr/bin/python3

import pdmt.mgr # for Mgr
import glob # for glob

mgr=pdmt.mgr.Mgr()

# debugging
#mgr.addHandler(pdmt.plugins.eventhandlers.debugger.EventHandler())
#mgr.addHandler(pdmt.plugins.nodehandlers.dirmaker.NodeHandler())

# c stuff
mgr.addHandler(pdmt.plugins.nodehandlers.chandler.NodeHandler())
node_exe=pdmt.plugins.nodetypes.cexecutablefilenode.NodeType(name='tests/main.elf')
mgr.addNode(node_exe)
mgr.addHandler(pdmt.plugins.nodehandlers.connector.NodeHandler(node_exe ,pdmt.plugins.nodetypes.objectfilenode.NodeType,'^tests/.*\.o$'))
node_c=pdmt.plugins.nodetypes.cfilenode.NodeType(name='tests/main.c')
mgr.addNode(node_c)

# mako stuff
mgr.addHandler(pdmt.plugins.nodehandlers.makohandler.NodeHandler())
for name in glob.glob('mako/*.mako'):
	mgr.addNode(pdmt.plugins.nodetypes.makofilenode.NodeType(name))

# clean stuff
mgr.addNode(pdmt.plugins.nodetypes.operations.clean.NodeType())

mgr.setDefaultNodeList([node_exe])

mgr.parseCmdline()
