#!/usr/bin/python

import pdmtcore.mgr
import pdmtcore.nodehandlers.chandler
import pdmtcore.nodehandlers.connector
import pdmtcore.nodetypes.sourcefilenode
import pdmtcore.nodetypes.objectfilenode
import pdmtcore.nodetypes.cexecutablefilenode
import pdmtcore.eventhandlers.debugger
import pdmtcore.cmdline
import pdmtcore.types

mgr=pdmtcore.mgr.Mgr()
mgr.addHandler(pdmtcore.nodehandlers.chandler.CHandler())
#mgr.addHandler(pdmtcore.eventhandlers.debugger.Debugger())
node=mgr.addNode(pdmtcore.nodetypes.cexecutablefilenode.CExecutableFileNode('tests/main.exe'))
mgr.addHandler(pdmtcore.nodehandlers.connector.Connector(node,pdmtcore.nodetypes.objectfilenode.ObjectFileNode,'^tests/.*\.o$'))
mgr.addNode(pdmtcore.nodetypes.sourcefilenode.SourceFileNode('tests/main.c',pdmtcore.types.t_c))
pdmtcore.cmdline.parse(mgr)
