import buildfilenode
import makofilenode
import pdmt.types

import pdmt.config
import config

import mako.template
import mako.lookup
import os # for os.chmod, os.unlink

class MakotFileNode(buildfilenode.BuildFileNode):
	def __init__(self,p_fname):
		super(MakotFileNode,self).__init__(p_fname,pdmt.types.t_makot)
	def build(self,mgr):
		for node in mgr.deps(self):
			if isinstance(node,makofilenode.MakoFileNode):
				p_input=node.fname
				break
		p_output=self.fname
		# remove the old file
		try:
			os.unlink(p_output)
		except:
			# handle the error better, only non existant file should be glossed over...
			pass
		input_encoding='utf-8'
		output_encoding='utf-8'
		mylookup=mako.lookup.TemplateLookup(directories=['.'],input_encoding=input_encoding,output_encoding=output_encoding)
		template=mako.template.Template(filename=p_input,lookup=mylookup,output_encoding=output_encoding,input_encoding=input_encoding)
		file=open(p_output,'w')
		# python 3
		#file.write((template.render_unicode(attributes={})))
		# python 2
		file.write(template.render(config=config))
		file.close()
		# python 3
		#os.chmod(p_output,0o0444)
		# python 2
		os.chmod(p_output,0444)
