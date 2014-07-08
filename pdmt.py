#!/usr/bin/python3

import pdmt.mgr # for Mgr
import glob # for glob

mgr=pdmt.mgr.Mgr()

# debugging
mgr.addHandler(pdmt.plugins.eventhandlers.debugger.EventHandler())
mgr.addHandler(pdmt.plugins.nodehandlers.dirmaker.NodeHandler())

# the 'all' target
node_all=pdmt.plugins.nodes.phony.NodeType(name='all')
mgr.addNode(node_all)
mgr.addHandler(pdmt.plugins.nodehandlers.connector.NodeHandler(
	cnode=node_all,
	type=pdmt.plugins.nodes.buildfile.NodeType,
))
mgr.setDefaultNodeList([node_all])

# c stuff
mgr.addHandler(pdmt.plugins.nodehandlers.chandler.NodeHandler())
node_exe=pdmt.plugins.nodes.cexecutablefile.NodeType(name='tests/main.elf')
mgr.addNode(node_exe)
mgr.addHandler(pdmt.plugins.nodehandlers.connector.NodeHandler(
	cnode=node_exe,
	type=pdmt.plugins.nodes.objectfile.NodeType,
	regexp='^tests/.*\.o$',
))
node_c=pdmt.plugins.nodes.cfile.NodeType(name='tests/main.c')
mgr.addNode(node_c)

# mako stuff
mgr.addHandler(pdmt.plugins.nodehandlers.makohandler.NodeHandler())
for name in glob.glob('mako/*.mako'):
	mgr.addNode(pdmt.plugins.nodes.makofile.NodeType(name))

# operations
mgr.addNode(pdmt.plugins.nodes.operations.clean.NodeType())
mgr.addNode(pdmt.plugins.nodes.operations.print_dot.NodeType())
mgr.addNode(pdmt.plugins.nodes.operations.gitclean.NodeType())

mgr.parseCmdline()
