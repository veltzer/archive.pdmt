import pdmt.plugins.nodes.build
import pdmt.plugins.nodes.file
import pdmt.utils.fileops


class NodeType(pdmt.plugins.nodes.file.NodeType, pdmt.plugins.nodes.build.NodeType):
    """
        a mixin class representing a node that can be built (not source)
    """

    def canClean(self):
        return True

    def clean(self, nbp):
        def dowork():
            pdmt.utils.fileops.unlinksoft(self.name)

        nbp.addFunction(dowork)

    def filebuild():
        raise ValueError('must override')

    def build(self, nbp):
        self.prebuild(nbp)
        self.filebuild(nbp)
        self.postbuild(nbp)

    ''' maybe make sure to unlink the file before the build '''
    ''' maybe we should create the folder before the build '''

    def prebuild(self, nbp):
        def dowork():
            pdmt.utils.fileops.unlinksoft(self.name)
            pdmt.utils.fileops.mkdirp(self.name)

        nbp.addFunction(dowork)

    def postbuild(self, nbp):
        def dowork():
            pdmt.utils.fileops.chmod_mw(self.name)
            pdmt.utils.fileops.checkexist_and_updatecache(self.name)

        nbp.addFunction(dowork)
