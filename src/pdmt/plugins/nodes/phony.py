import pdmt.api # for NodeType

'''
This node represents a node which is not on disk or in any persistent storage.
It is usually used to connect other nodes.
like .PHONY in gmake...:)
'''

class NodeType(pdmt.api.NodeType):
    def __init__(self, **kw):
        super().__init__(proto='phony', **kw)
    def needbuild(self,todo):
        return True
    def canBuild(self):
        return True
    def build(self, nbp):
        pass
    def canClean(self):
        return False
