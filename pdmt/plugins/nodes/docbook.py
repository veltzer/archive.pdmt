import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.cfile # for NodeType

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	def filebuild(self, nbp):
		s='xsltproc /usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook.xsl {input} | fop -fo - -pdf {output}'.format(
			input=self.getSource().name,
			output=self.name,
		)
		nbp.addCmdString(s)
