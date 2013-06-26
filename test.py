#!/usr/bin/python3

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

import glob
import os # for os.environ

import pdmt.operations.installaptsite
import pdmt.operations.depsinstaller
import pdmt.operations.debmaker
import pdmt.operations.debinstaller
import pdmt.operations.hello
import pdmt.operations.gitclean

mgr=pdmt.mgr.Mgr()
mgr.addHandler(pdmt.nodehandlers.chandler.CHandler())
mgr.addHandler(pdmt.nodehandlers.makohandler.MakoHandler())
if os.environ.get("PDMT_DEBUG") != None:
	mgr.addHandler(pdmt.eventhandlers.debugger.Debugger())
node=mgr.addNode(pdmt.nodetypes.cexecutablefilenode.CExecutableFileNode('tests/main.exe'))
mgr.addHandler(pdmt.nodehandlers.connector.Connector(node,pdmt.nodetypes.objectfilenode.ObjectFileNode,'^tests/.*\.o$'))
mgr.addNode(pdmt.nodetypes.cfilenode.CFileNode('tests/main.c'))

# mako stuff
nodes=[]
for name in glob.glob('mako/*.mako'):
	nodes.append(mgr.addNode(pdmt.nodetypes.makofilenode.MakoFileNode(name)))

mgr.addOperation(
	pdmt.operations.installaptsite.InstallAptSite(),
	#mgr.dependsOn(nodes),
	mgr.dependsOn([]),
)
mgr.addOperation(
	pdmt.operations.depsinstaller.DepsInstaller(),
	mgr.dependsOn([]),
)
mgr.addOperation(
	pdmt.operations.debmaker.DebMaker(),
	mgr.dependsOn([]),
)
mgr.addOperation(
	pdmt.operations.debinstaller.DebInstaller(),
	mgr.dependsOn([]),
)
mgr.addOperation(
	pdmt.operations.hello.Hello(),
	mgr.dependsOn([]),
)
mgr.addOperation(
	pdmt.operations.gitclean.GitClean(),
	mgr.dependsOn([]),
)

pdmt.cmdline.parse(mgr)
