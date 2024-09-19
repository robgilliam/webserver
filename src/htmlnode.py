class HTMLNode:
	def __init__(self, tag = None, value = None, children = None, props = None):
			self.tag = tag
			self.value = value
			self.children = children
			self.props = props

	def __eq__(self, other):
		return (self.tag == other.tag
				and self.value == other.value
				and self.children == other.children
				and self.props == other.props)

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		html_props = ""
		if self.props is not None:
			for prop_string in map(lambda prop: f" {prop[0]}=\"{prop[1]}\"", self.props.items()):
				html_props += prop_string
		return html_props
