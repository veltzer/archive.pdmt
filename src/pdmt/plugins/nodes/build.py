import pdmt.api


class NodeType(pdmt.api.NodeType):
    def canBuild(self):
        return True
