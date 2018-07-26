from docutils import nodes


class helloworld(nodes.Admonition, nodes.Element):
    pass


def visit_helloworld_node(self, node):
    self.visit_admonition(node)


def depart_helloworld_node(self, node):
    self.depart_admonition(node)
