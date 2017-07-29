import pdmt.plugins.nodes.operation
import pdmt.utils.subproc


class NodeType(pdmt.plugins.nodes.operation.NodeType):
    """
    A git cleaning operation
    """
    def __init__(self, **kw):
        super().__init__(name='gitclean', description='very forceful git clean of a repository', **kw)

    def build(self, nbp):
        args = self.createArgs()
        args.append('git')
        args.append('clean')
        args.append('-xdf')
        nbp.addCmdList(args)
