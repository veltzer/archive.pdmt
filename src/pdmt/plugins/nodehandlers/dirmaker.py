import pdmt.api # for NodeHandler
import pdmt.event # for Event
import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.utils.fileops # for mkdirparent_file

'''
This handler makes sure to create folders for files before running their build.
Not sure if this is the right design. Maybe it's better that builders simply
run a pre-hook in their build method and target output file will do all that
work for them. This fits in better with the fact that we may want to check
after building each target that it is there.
'''

class NodeHandler(pdmt.api.NodeHandler):
    def respond(self,data=None,eventtype=None):
        if eventtype!=pdmt.event.Event.nodeprebuild:
            return
        node=data
        if not isinstance(node,pdmt.plugins.nodes.buildfile.NodeType):
            return
        pdmt.utils.fileops.mkdirparent_file(node.name)
