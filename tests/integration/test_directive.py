import pytest

pytestmark = pytest.mark.sphinx('html', testroot='directive')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
def test_index(page):
    # Make sure the page title is what you expect
    title = page.find('h1').contents[0].strip()
    assert 'Directive Test' == title

    # Now test the directive
    directive = page.find('em').contents[0].strip()
    assert 'Hello World' == directive
