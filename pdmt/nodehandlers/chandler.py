import pdmt.nodetypes.cfilenode
import pdmt.nodetypes.objectfilenode

import pdmt.config

class CHandler:
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmt.nodetypes.cfilenode.CFileNode):
			return
		newname=node.m_fname[:node.m_fname.rfind(pdmt.config.ns_chandler.p_sourcefilesuffix)]+pdmt.config.ns_chandler.p_objectfilesuffix
		newnode=pdmt.nodetypes.objectfilenode.ObjectFileNode(newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))
