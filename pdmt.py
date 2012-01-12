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
mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/test.mako'))
mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/distributions.mako'))
mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/index.php.mako'))
mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode('mako/options.mako'))

pdmt.cmdline.parse(mgr)
