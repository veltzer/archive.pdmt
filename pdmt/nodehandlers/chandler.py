import pdmt.nodetypes.filenode

class CHandler:
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmt.nodetypes.filenode.FileNode):
			return
		if not node.fname.endswith('.c'):
			return
		newname=node.fname[:node.fname.rfind('.c')]+'.o'
		newnode=pdmt.nodetypes.filenode.FileNode(newname)
		mgr.addNode(newnode)
		mgr.addEdge((node,newnode))
