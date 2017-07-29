import os.path

import pdmt.api


class NodeType(pdmt.api.NodeType):
    """
    A file node. Anything which is a file should mix in this one.
    """
    def __init__(self, **kw):
        super().__init__(proto='file', **kw)

    def get_lmt(self):
        # if the file does not exist then lmt is very old:
        if not os.path.isfile(self.name):
            return float(0)
        else:
            return pdmt.utils.fileops.getmtime(self.name)
