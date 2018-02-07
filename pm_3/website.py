from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHnadler(ContentHandler):
	def startElement(self, name, attrs):
		print(name,attrs.keys())

parse('website.xml',TestHnadler())