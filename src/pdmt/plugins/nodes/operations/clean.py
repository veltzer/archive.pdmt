import pdmt.plugins.nodes.operation # for NodeType

'''
A generic clean node for Pdmt
'''

class NodeType(pdmt.plugins.nodes.operation.NodeType):
    def __init__(self, **kw):
        super().__init__(name='clean', description='clean all nodes', **kw)
    def build(self, nbp):
        build_list=self.mgr.get_clean_node_list_sorted()
        lst_len=len(build_list)
        self.mgr.progress('going to clean [{lst_len}] {plural}...'.format(
            lst_len=lst_len,
            plural=pdmt.utils.lang.plural('node', lst_len),
        ))
        for i,node in enumerate(build_list):
            node.clean(nbp)
