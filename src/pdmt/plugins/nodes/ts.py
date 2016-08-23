import pdmt.api # for NodeType
import dbm.gnu # for open
import time # for time

'''
This node is a node for which only a time stamp is stored
in a central managed db.
It is usually used as a time stamp node for collecting many nodes
together.
'''

handle=None
def init(mgr):
    global handle
    # 'c' means rw + create if needed
    handle=dbm.gnu.open('.ts.gdbm', 'c')

def fini(mgr):
    global handle
    handle.close()

class NodeType(pdmt.api.NodeType):
    def __init__(self, **kw):
        super().__init__(proto='ts', **kw)
    def get_lmt(self):
        if self.name in handle:
            return float(handle[self.name])
        else:
            return float(0)
    def canBuild(self):
        return True
    def build(self, nbp):
        def dowork():
            global handle
            handle[self.name]=str(time.time())
        nbp.addFunction(dowork)
    def canClean(self):
        return True
    def clean(self, nbp):
        def dowork():
            global handle
            if self.name in handle:
                del handle[self.name]
        nbp.addFunction(dowork)


''' a method to debug this module '''
def print_all_entries():
    global handle
    # show all key value pairs
    k=handle.firstkey()
    while k is not None:
        print(k.decode(), handle[k].decode())
        k=handle.nextkey(k)
