"""

Integration-oriented fixtures for sphinx.testing of
generated HTML.

"""

import os

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.path import path

pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture()
def rootdir():
    roots = path(os.path.dirname(__file__) or '.').abspath() / 'roots'
    yield roots


@pytest.fixture()
def content(app):
    app.build()
    yield app


@pytest.fixture()
def page(content, request) -> BeautifulSoup:
    pagename = request.param
    c = (content.outdir / pagename).text()

    yield BeautifulSoup(c, 'html5lib')
