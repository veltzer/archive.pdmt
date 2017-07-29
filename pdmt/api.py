import pdmt.prn
import pdmt.mgr
import pdmt.arguments


# the inheritance from 'object' is very important to get the __class__
# and other stuff we need in order for OO to work properly...
class NodeType(object):
    def __init__(self, type=None, name=None, description=None, proto=None):
        super().__init__()
        self.mgr = pdmt.mgr.Mgr.get_manager()
        if type is None:
            self.type = 'unset'
        else:
            self.type = type
        if proto is None:
            self.proto = 'node'
        else:
            self.proto = proto
        if name is None:
            self.name = 'unset'
        else:
            self.name = name
        if description is None:
            self.description = 'unset'
        else:
            self.description = description
        self.mgr.add_node(self)

    def get_name(self):
        return pdmt.prn.create(
            proto=self.proto,
            name=self.name
        )

    def needbuild(self, todo):
        # lets compare dates
        rebuild = False
        for node in self.getDeps():
            if node in todo:
                rebuild = True
                break
            if node.get_lmt() > self.get_lmt():
                rebuild = True
                break
        return rebuild

    def canBuild(self):
        raise ValueError('must override')

    def build(self, nbp):
        raise ValueError('must override')

    def canClean(self):
        raise ValueError('must override')

    def clean(self, nbp):
        raise ValueError('must override')

    def get_lmt(self):
        return float(0)

    def getDeps(self):
        return self.mgr.deps(self)

    def getDepsYield(self):
        for node in self.mgr.depsYield(self):
            yield node

    def getSource(self):
        ret = self.getDeps()
        if len(ret) != 1:
            raise ValueError('too many sources')
        return ret[0]

    def getSourcesOfType(self, type):
        ret = []
        for node in self.getDeps():
            if isinstance(node, type):
                ret.append(node)
        return ret

    def getSourceOfType(self, type):
        ret = self.getSourcesOfType(type)
        if len(ret) != 1:
            raise ValueError('too many sources')
        return ret[0]

    def createArgs(self):
        return pdmt.arguments.Arguments(self.mgr)


'''
This is the base class of all node handlers within the system
'''


class NodeHandler(object):
    def __init__(self):
        super().__init__()
        self.mgr = pdmt.mgr.Mgr.get_manager()
        self.mgr.addHandler(self)

    def respond(self, data=None, eventtype=None):
        raise ValueError('must override')


'''
This is the base class of all event handlers within the system
'''


class EventHandler(object):
    def __init__(self):
        super().__init__()
        self.mgr = pdmt.mgr.Mgr.get_manager()

    def respond(self, data=None, eventtype=None):
        raise ValueError('must override')


class Cache(object):
    """
    This is the cache handler
    """
    def __init__(self):
        super().__init__()
        self.mgr = pdmt.mgr.Mgr.get_manager()

    def has_checksum(self, checksum):
        raise ValueError('must override')

    def get_filename(self, checksum, filename):
        raise ValueError('must override')

    def put_filename(self, checksum, filename):
        raise ValueError('must override')
