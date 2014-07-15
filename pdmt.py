#!/usr/bin/python3

import pdmt.mgr # for Mgr
import glob # for glob

mgr=pdmt.mgr.Mgr()

# debugging
pdmt.plugins.eventhandlers.debugger.EventHandler(mgr=mgr)
pdmt.plugins.nodehandlers.dirmaker.NodeHandler(mgr=mgr)

# the 'all' target
node_all=pdmt.plugins.nodes.ts.NodeType(mgr=mgr,name='all')
pdmt.plugins.nodehandlers.connector.NodeHandler(
	mgr=mgr,
	cnode=node_all,
	type=pdmt.plugins.nodes.buildfile.NodeType,
)
mgr.setDefaultNodeList([node_all])

# c stuff
pdmt.plugins.nodehandlers.onetoone.NodeHandler(
	mgr=mgr,
	type=pdmt.plugins.nodes.cfile.NodeType,
	suffix='.o',
	same_folder=True,
	target_type=pdmt.plugins.nodes.objectfile.NodeType,
)
node_exe=pdmt.plugins.nodes.cexecutablefile.NodeType(mgr=mgr, name='tests/main.elf')
pdmt.plugins.nodehandlers.connector.NodeHandler(
	mgr=mgr,
	cnode=node_exe,
	type=pdmt.plugins.nodes.objectfile.NodeType,
	regexp='^tests/.*\.o$',
)
pdmt.plugins.nodes.cfile.NodeType(mgr=mgr, name='tests/main.c')

# mako stuff
pdmt.plugins.nodehandlers.onetoone.NodeHandler(
	mgr=mgr,
	type=pdmt.plugins.nodes.makofile.NodeType,
	suffix='',
	same_folder=False,
	folder='makot',
	target_type=pdmt.plugins.nodes.makotfile.NodeType,
)
for name in glob.glob('mako/*.mako'):
	pdmt.plugins.nodes.makofile.NodeType(mgr=mgr, name=name)

# operations
pdmt.plugins.nodes.operations.clean.NodeType(mgr=mgr)
pdmt.plugins.nodes.operations.print_dot.NodeType(mgr=mgr)
pdmt.plugins.nodes.operations.gitclean.NodeType(mgr=mgr)

mgr.parseCmdline()

mgr.shutdown()
