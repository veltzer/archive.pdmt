import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.makofile # for NodeType
import mako.template # for Template
import mako.lookup # for TemplateLookup
import pdmt.utils.fileops # for unlinksoft

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
    def filebuild(self, nbp):
        def dowork():
            p_input=self.getSourceOfType(pdmt.plugins.nodes.makofile.NodeType).name
            input_encoding='utf-8'
            output_encoding='utf-8'
            mylookup=mako.lookup.TemplateLookup(directories=['.'],input_encoding=input_encoding,output_encoding=output_encoding)
            template=mako.template.Template(filename=p_input,lookup=mylookup,output_encoding=output_encoding,input_encoding=input_encoding)
            file=open(self.name,'w')
            # python 3
            #file.write((template.render_unicode(attributes={})))
            # python 2
            try:
                file.write(str(template.render(pdmt=pdmt)))
            except Exception as e:
                file.close()
                pdmt.utils.fileops.unlinksoft(self.name)
            #    # TODO: self.error(e)
                raise e
            file.close()
        nbp.addFunction(dowork)
