import pdmt.plugins.nodes.operation


class NodeType(pdmt.plugins.nodes.operation.NodeType):
    """
    An operation to print the graph in dot notation
    """
    def __init__(self, **kw):
        super().__init__(name='print_dot', description='print graph in dot notation', **kw)

    def build(self, nbp):
        def dowork():
            self.mgr.print_dot()

        nbp.addFunction(dowork)
