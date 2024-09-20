from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode has no children")

        content = "".join(map(lambda child: child.to_html(), self.children))

        return f"<{self.tag}{self.props_to_html()}>{content}</{self.tag}>"
