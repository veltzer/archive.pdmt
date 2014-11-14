import pdmt.plugins.nodes.buildfile # for NodeType
import pdmt.plugins.nodes.cfile # for NodeType

class NodeType(pdmt.plugins.nodes.buildfile.NodeType):
	def filebuild(self, nbp):
		# validation of the xml
		s='xmlstarlet val --err --xsd /usr/share/xml/docbook/schema/xsd/5.0/docbook.xsd {input}'.format(
			input=self.getSource().name,
		)
		nbp.addCmdString(s)
		# from xml to fo and then to pdf
		s='xsltproc /usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook.xsl {input} | fop -fo - -pdf {output}'.format(
			input=self.getSource().name,
			output=self.name,
		)
		nbp.addCmdString(s)
