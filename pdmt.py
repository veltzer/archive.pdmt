#!/usr/bin/python3

import pdmt.mgr # for Mgr
import glob # for glob

mgr=pdmt.mgr.Mgr.new_manager()

# debugging
pdmt.plugins.eventhandlers.debugger.EventHandler()
pdmt.plugins.nodehandlers.dirmaker.NodeHandler()

# the 'all' target
node_ts_all=pdmt.plugins.nodes.ts.NodeType(name='all')
pdmt.plugins.nodehandlers.connector.NodeHandler(
	cnode=node_ts_all,
	type=pdmt.plugins.nodes.buildfile.NodeType,
)

# c stuff
pdmt.plugins.nodehandlers.onetoone.NodeHandler(
	type=pdmt.plugins.nodes.cfile.NodeType,
	suffix='.o',
	same_folder=True,
	target_type=pdmt.plugins.nodes.objectfile.NodeType,
)
node_exe=pdmt.plugins.nodes.cexecutablefile.NodeType(name='tests/main.elf')
pdmt.plugins.nodehandlers.connector.NodeHandler(
	cnode=node_exe,
	type=pdmt.plugins.nodes.objectfile.NodeType,
	regexp='^tests/.*\.o$',
)
pdmt.plugins.nodes.cfile.NodeType(name='tests/main.c')

# docbook stuff
docbook_xml=pdmt.plugins.nodes.sourcefile.NodeType(name='docbook/pdmt.xml')
docbook_pdf=pdmt.plugins.nodes.docbook.NodeType(name='docbook/pdmt.pdf')
mgr.add_edge((docbook_pdf, docbook_xml))

# operations
node_op_clean=pdmt.plugins.nodes.operations.clean.NodeType()
node_op_print_dot=pdmt.plugins.nodes.operations.print_dot.NodeType()
node_op_gitclean=pdmt.plugins.nodes.operations.gitclean.NodeType()

# clean
node_phony_clean=pdmt.plugins.nodes.phony.NodeType(name='clean')
mgr.add_edge((node_phony_clean, node_op_clean))
#mgr.add_edge((node_phony_clean, node_op_gitclean))

# all
node_phony_all=pdmt.plugins.nodes.phony.NodeType(name='all')
mgr.add_edge((node_phony_all, node_ts_all))

mgr.parseCmdline()

mgr.shutdown()
