from docutils.parsers.rst import Directive

from customizing_sphinx.node import helloworld


class HelloWorldDirective(Directive):

    def run(self):
        hello_world_node = helloworld('Hello World')
        self.state.nested_parse(self.content, self.content_offset,
                                hello_world_node)

        return [hello_world_node]
