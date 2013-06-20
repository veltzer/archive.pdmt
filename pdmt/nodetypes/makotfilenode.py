import pdmt.nodetypes.buildfilenode
import pdmt.nodetypes.makofilenode
import pdmt.types

import pdmt.config

import mako.template
import mako.lookup
import pdmt.utils.fileops

class MakotFileNode(pdmt.nodetypes.buildfilenode.BuildFileNode):
	def __init__(self,p_fname):
		super(MakotFileNode,self).__init__(p_fname,pdmt.types.t_makot)
	def deps(self):
		p_input=getSingleSourceOfType(self,makofilenode.MakoFileNode)
	def build(self):
		p_input=self.getSourceOfType(pdmt.nodetypes.makofilenode.MakoFileNode).m_fname
		p_output=self.m_fname
		# remove the old file
		pdmt.utils.fileops.unlinksoft(p_output)
		input_encoding='utf-8'
		output_encoding='utf-8'
		mylookup=mako.lookup.TemplateLookup(directories=['.'],input_encoding=input_encoding,output_encoding=output_encoding)
		template=mako.template.Template(filename=p_input,lookup=mylookup,output_encoding=output_encoding,input_encoding=input_encoding)
		file=open(p_output,'w')
		# python 3
		#file.write((template.render_unicode(attributes={})))
		# python 2
		try:
			file.write(str(template.render(pdmt=pdmt)))
		except Exception as e:
			file.close()
			pdmt.utils.fileops.unlinksoft(p_output)
			# TODO: self.error(e)
			raise e
		file.close()
		pdmt.utils.fileops.chmod(p_output,0o0444)
