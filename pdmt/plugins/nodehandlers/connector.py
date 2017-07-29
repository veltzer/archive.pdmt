import pdmt.api
import re


class NodeHandler(pdmt.api.NodeHandler):
    """
    This is a node connector. It listens for Event.nodepostadd events
    and connects nodes that match a regualr expression to the node
    given to it at construction.

    TODO: It should also listen for the removal of the node given to it
    and remove itself when it is removed.
    """

    def __init__(self, cnode=None, type=None, regexp=None, **kw):
        super().__init__(**kw)
        self.cnode = cnode
        self.type = type
        self.regexp = regexp
        if self.regexp is not None:
            self.cregexp = re.compile(self.regexp)

    def respond(self, data=None, event_type=None):
        if event_type != pdmt.event.Event.nodepostadd:
            return
        node = data
        if self.type is not None and not isinstance(node, self.type):
            return
        if self.regexp is not None and not self.cregexp.match(node.name):
            return
        self.mgr.add_edge((self.cnode, node))
