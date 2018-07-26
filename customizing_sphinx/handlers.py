from docutils import nodes

from customizing_sphinx.node import helloworld


def process_helloworld_nodes(app, doctree, fromdocname):
    for hwnode in doctree.traverse(helloworld):
        output = f'<em>{hwnode.rawsource}</em>'
        hwnode.replace_self(nodes.raw('', output, format='html'))
