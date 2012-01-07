import pdmtcore.nodetypes.objectfilenode

class CHandler:
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmtcore.nodetypes.filenode.FileNode):
			return
		if not node.fname.endswith('.c'):
			return
		newname=node.fname[:node.fname.rfind('.c')]+'.o'
		newnode=pdmtcore.nodetypes.objectfilenode.ObjectFileNode(newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))
