#!/usr/bin/python

import pdmt.mgr
import pdmt.nodehandlers.chandler
import pdmt.nodehandlers.makohandler
import pdmt.nodehandlers.connector
import pdmt.nodetypes.cfilenode
import pdmt.nodetypes.makofilenode
import pdmt.nodetypes.objectfilenode
import pdmt.nodetypes.cexecutablefilenode
import pdmt.eventhandlers.debugger
import pdmt.operations.installaptsite
import pdmt.cmdline
import glob

mgr=pdmt.mgr.Mgr()
mgr.addHandler(pdmt.nodehandlers.chandler.CHandler())
mgr.addHandler(pdmt.nodehandlers.makohandler.MakoHandler())
#mgr.addHandler(pdmt.eventhandlers.debugger.Debugger())
node=mgr.addNode(pdmt.nodetypes.cexecutablefilenode.CExecutableFileNode('tests/main.exe'))
mgr.addHandler(pdmt.nodehandlers.connector.Connector(node,pdmt.nodetypes.objectfilenode.ObjectFileNode,'^tests/.*\.o$'))
mgr.addNode(pdmt.nodetypes.cfilenode.CFileNode('tests/main.c'))

# mako stuff
nodes=[]
for name in glob.glob('mako/*.mako'):
	nodes.append(mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode(name)))

mgr.addOperation(
	pdmt.operations.installaptsite.InstallAptSite(
		'installaptsite',
		'install the apt site',
		nodes[0],
		nodes[1],
		nodes[2]),
	mgr.dependsOn(nodes),
)

pdmt.cmdline.parse(mgr)
