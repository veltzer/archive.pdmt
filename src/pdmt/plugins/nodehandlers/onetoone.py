import pdmt.api # for NodeHandler
import pdmt.event # for Event
import pdmt.plugins.nodes.cfile # for NodeType
import pdmt.plugins.nodes.objectfile # for NodeType
import pdmt.utils.filenames # for replace_suffix, replace_suffix_new_folder

class NodeHandler(pdmt.api.NodeHandler):
	def __init__(self,type=None,same_folder=True,suffix=None,target_type=None,folder=None, **kw):
		super().__init__(**kw)
		self.type=type
		self.same_folder=same_folder
		self.suffix=suffix
		self.target_type=target_type
		self.folder=folder
	def respond(self,data=None,eventtype=None):
		if eventtype!=pdmt.event.Event.nodepostadd:
			return
		node=data
		if not isinstance(node,self.type):
			return
		if self.same_folder:
			newname=pdmt.utils.filenames.replace_suffix(node.name, self.suffix)
		else:
			newname=pdmt.utils.filenames.replace_suffix_new_folder(node.name, self.suffix, self.folder)
		newnode=self.target_type(name=newname)
		self.mgr.add_edge((newnode,node))