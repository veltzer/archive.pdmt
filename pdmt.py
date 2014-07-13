#!/usr/bin/python3

import pdmt.mgr # for Mgr
import glob # for glob

mgr=pdmt.mgr.Mgr()

# debugging
mgr.addHandler(pdmt.plugins.eventhandlers.debugger.EventHandler())
mgr.addHandler(pdmt.plugins.nodehandlers.dirmaker.NodeHandler())

# the 'all' target
node_all=pdmt.plugins.nodes.ts.NodeType(name='all')
mgr.addHandler(pdmt.plugins.nodehandlers.connector.NodeHandler(
	cnode=node_all,
	type=pdmt.plugins.nodes.buildfile.NodeType,
))
mgr.setDefaultNodeList([node_all])

# c stuff
mgr.addHandler(pdmt.plugins.nodehandlers.onetoone.NodeHandler(
	type=pdmt.plugins.nodes.cfile.NodeType,
	suffix='.o',
	same_folder=True,
	target_type=pdmt.plugins.nodes.objectfile.NodeType,
))
node_exe=pdmt.plugins.nodes.cexecutablefile.NodeType(name='tests/main.elf')
mgr.addHandler(pdmt.plugins.nodehandlers.connector.NodeHandler(
	cnode=node_exe,
	type=pdmt.plugins.nodes.objectfile.NodeType,
	regexp='^tests/.*\.o$',
))
node_c=pdmt.plugins.nodes.cfile.NodeType(name='tests/main.c')

# mako stuff
mgr.addHandler(pdmt.plugins.nodehandlers.onetoone.NodeHandler(
	type=pdmt.plugins.nodes.makofile.NodeType,
	suffix='',
	same_folder=False,
	folder='makot',
	target_type=pdmt.plugins.nodes.makotfile.NodeType,
))
for name in glob.glob('mako/*.mako'):
	pdmt.plugins.nodes.makofile.NodeType(name=name)

# operations
pdmt.plugins.nodes.operations.clean.NodeType()
pdmt.plugins.nodes.operations.print_dot.NodeType()
pdmt.plugins.nodes.operations.gitclean.NodeType()

mgr.parseCmdline()

mgr.shutdown()
