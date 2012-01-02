#!/usr/bin/python

import pdmt.mgr
import pdmt.nodehandlers.chandler
import pdmt.nodehandlers.connector
import pdmt.nodetypes.sourcefilenode
import pdmt.nodetypes.objectfilenode
import pdmt.nodetypes.cexecutablefilenode
import pdmt.eventhandlers.debugger

mgr=pdmt.mgr.Mgr()
mgr.addHandler(pdmt.nodehandlers.chandler.CHandler())
#mgr.addHandler(pdmt.eventhandlers.debugger.Debugger())
node=mgr.addNode(pdmt.nodetypes.cexecutablefilenode.CExecutableFileNode('tests/main.exe'))
mgr.addHandler(pdmt.nodehandlers.connector.Connector(node,pdmt.nodetypes.objectfilenode.ObjectFileNode,'^tests/.*\.o$'))
mgr.addNode(pdmt.nodetypes.sourcefilenode.SourceFileNode('tests/main.c'))
#mgr.printme()
mgr.build()
