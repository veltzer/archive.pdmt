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
import pdmt.types

mgr=pdmt.mgr.Mgr()
mgr.addHandler(pdmt.nodehandlers.chandler.CHandler())
mgr.addHandler(pdmt.nodehandlers.makohandler.MakoHandler())
#mgr.addHandler(pdmt.eventhandlers.debugger.Debugger())
node=mgr.addNode(pdmt.nodetypes.cexecutablefilenode.CExecutableFileNode('tests/main.exe'))
mgr.addHandler(pdmt.nodehandlers.connector.Connector(node,pdmt.nodetypes.objectfilenode.ObjectFileNode,'^tests/.*\.o$'))
mgr.addNode(pdmt.nodetypes.cfilenode.CFileNode('tests/main.c'))

# mako stuff
node=mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/test.mako'))

node1=mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/distributions.mako'))
node2=mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/index.php.mako'))
node3=mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/options.mako'))

mgr.addOperation(
	pdmt.operations.installaptsite.InstallAptSite(
		'installaptsite',
		'install the apt site',
		node1,
		node2,
		node3),
	mgr.dependsOn([node1,node2,node3]),
)

pdmt.cmdline.parse(mgr)
