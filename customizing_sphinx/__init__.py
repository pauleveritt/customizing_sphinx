from customizing_sphinx.directive import HelloWorldDirective
from customizing_sphinx.handlers import process_helloworld_nodes
from customizing_sphinx.node import (
    helloworld,
    depart_helloworld_node,
    visit_helloworld_node
)


def setup(app):
    app.add_node(
        helloworld,
        html=(visit_helloworld_node, depart_helloworld_node),
    )
    app.add_directive('helloworld', HelloWorldDirective)
    app.connect('doctree-resolved', process_helloworld_nodes)
