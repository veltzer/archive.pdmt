import pdmt.api
import pdmt.event
import pdmt.plugins.nodes.cfile
import pdmt.plugins.nodes.objectfile
import pdmt.utils.filenames


class NodeHandler(pdmt.api.NodeHandler):
    def __init__(self, type=None, same_folder=True, suffix=None, target_type=None, folder=None, **kw):
        super().__init__(**kw)
        self.type = type
        self.same_folder = same_folder
        self.suffix = suffix
        self.target_type = target_type
        self.folder = folder

    def respond(self, data=None, eventtype=None):
        if eventtype != pdmt.event.Event.nodepostadd:
            return
        node = data
        if not isinstance(node, self.type):
            return
        if self.same_folder:
            new_name = pdmt.utils.filenames.replace_suffix(node.name, self.suffix)
        else:
            new_name = pdmt.utils.filenames.replace_suffix_new_folder(node.name, self.suffix, self.folder)
        new_node = self.target_type(name=new_name)
        self.mgr.add_edge((new_node, node))
