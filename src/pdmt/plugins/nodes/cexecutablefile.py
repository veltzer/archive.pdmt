import pdmt.plugins.nodes.buildfile
import pdmt.plugins.nodes.objectfile


class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
    @classmethod
    def init(cls, mgr):
        mgr.addTypedConfigDep(cls, 'LD')
        mgr.addTypedConfigDep(cls, 'LDFLAGS')

    def filebuild(self, nbp):
        args = self.createArgs()
        args.appendConfig('LD')
        args.append('-o')
        args.append(self.name)
        args.appendConfigIfNotEmpty('LDFLAGS')
        for node in self.getSourcesOfType(pdmt.plugins.nodes.objectfile.NodeType):
            args.append(node.name)
        nbp.addCmdList(args)
