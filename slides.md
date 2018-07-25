# Customizing Sphinx

### Simple, Normal, Hard

##### Paul Everitt, @paulweveritt

Follow Along: URL

----  ----

## About Me

- PyCharm Developer Advocate
- Go back a ways in Python

----

## Raise Your Hand If You...


* Have ever written Sphinx docs? <!-- .element: class="fragment" -->
* Customized a Sphinx site? <!-- .element: class="fragment" -->
* Written a Sphinx extension? <!-- .element: class="fragment"-->
* Cursed because the RST docs are on a SourceForge page which is down for weeks cuz lolz sourceforge <!-- .element: class="fragment" --> 

----

## Today

- Sphinx: the tool, the engine
- Simple (``conf.py``)
- Normal (overrides)
- Hard (extensions)

----

### About Sphinx

- Static site generator
- Documentation and more
- Several killer features
    - Intra/inter-linking
- Extensible, but crazy-old stack

----

![](images/structuredtext.png)


----  ----

## 1. Simple: Configuration

- Change some configuration values
- Change some theme options

----  ----

### 1a. conf.py

- TODO include some conf.py

Note:
- Sphinx is driven by conf file

----

### If your site looks like this...

- TODO screenshot

----

### ...and we change project title

```python
# -- Project information ---------------------

project = 'Customizing Sphinx'
copyright = '2018, Paul Everitt <pauleveritt@me.com>'
author = 'Paul Everitt <pauleveritt@me.com>'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''
```

<span class="fragment" data-code-focus="1">
...from this:
</span>

----

### ...and we change project title

```python
project = 'Customizing Sphinx'
copyright = '2018, Paul Everitt <pauleveritt@me.com>'
author = 'Paul Everitt <pauleveritt@me.com>'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''
```

<span class="fragment" data-code-focus="1">
...to this:
</span>


----

### After rebuilding, looks like:

TODO screenshot


----

### What other knobs can I change?

TODO code snippet of some other knobs.

----  ----


### 1b. Change some theme options

```python
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
```

- Theme: Another thing I can change
- Where are the ``html_theme_options``?

Notes:
- Good luck finding them

----

### Sphinx HTML theming

TODO screenshot of Sphinx HTML theming page

Notes:
- Show the theme.conf part

----

### Alabaster Customization

TODO Screenshot http://alabaster.readthedocs.io/en/latest/customization.html

Alabaster has lots of ways to customize.

----

### Its theme options are documented:

TODO screenshot of http://alabaster.readthedocs.io/en/latest/customization.html#theme-options

----

### Its ``theme.conf`` file

TODO https://github.com/bitprophet/alabaster/blob/master/alabaster/theme.conf

Because docs get out of date.

Notes:
- This is a mini-DSL with a validation system


----

### If I change the page width

TODO conf.py with html_theme_options


----

### It looks like this

TODO screenshot

----

#### alabaster/static/alabaster.css_t

TODO screenshot of https://github.com/bitprophet/alabaster/blob/master/alabaster/static/alabaster.css_t#L58

---- 

#### Let's make an error

TODO conf.py with invalid option and highlighting

----

### Rebuild shows

TODO code-block bash of terminal with error in build


----  ----

## 2. Normal: Customizing

- Override a template
- Add some CSS
- Install an extension
- Install a content-oriented extension

----  ----


### 2a. Override a template

TODO Annotated screenshot of where to put a paragraph

I'd like to put a paragraph there.
 

----

### Hold on to your butts

TODO giphy for hold onto your butts


----

### ``albaster/layout.html``
 
```html+jinja 
{%- extends "basic/layout.html" %}

{%- block extrahead %}
  {{ super() }}
  <link rel="stylesheet" href="{{ pathto('_static/custom.css', 1) }}" type="text/css" />
  {% if theme_touch_icon %}
    <link rel="apple-touch-icon" href="{{ pathto('_static/' ~ theme_touch_icon, 1) }}" />
  {% endif %}
  {% if theme_canonical_url %}
    <link rel="canonical" href="{{ theme_canonical_url }}{{ pagename }}.html"/>
  {% endif %}
  <meta name="viewport" content="width=device-width, initial-scale=0.9, maximum-scale=0.9" />
{% endblock %}

{# top+bottom related navs; we also have our own in sidebar #}
{%- macro rellink_markup() %}
  <nav id="rellinks">
    <ul>
      {%- if prev %}
        <li>
          &larr;
          <a href="{{ prev.link|e }}" title="Previous document">{{ prev.title }}</a>
        </li>
      {%- endif %}
      {%- if next %}
        <li>
          <a href="{{ next.link|e }}" title="Next document">{{ next.title }}</a>
          &rarr;
        </li>
      {%- endif %}
    </ul>
  </nav>
{%- endmacro %}

{%- set theme_show_relbar_top = theme_show_relbar_top or theme_show_relbars %}
{%- set theme_show_relbar_bottom = theme_show_relbar_bottom or theme_show_relbars %}

{# removed existing top+bottom related nav, and embed in main content #}
{%- block relbar1 %}{% endblock %}
{%- block relbar2 %}{% endblock %}

{# Nav should appear before content, not after #}
{%- block content %}
{%- if theme_fixed_sidebar|lower == 'true' %}
  <div class="document">
    {{ sidebar() }}
    {%- block document %}
      <div class="documentwrapper">
      {%- if render_sidebar %}
        <div class="bodywrapper">
      {%- endif %}

          {%- block relbar_top %}
            {%- if theme_show_relbar_top|tobool %}
              <div class="related top">
                &nbsp;
                {{- rellink_markup () }}
              </div>
            {%- endif %}
          {% endblock %}

          <div class="body" role="main">
            {% block body %} {% endblock %}
          </div>

          {%- block relbar_bottom %}
            {%- if theme_show_relbar_bottom|tobool %}
              <div class="related bottom">
                &nbsp;
                {{- rellink_markup () }}
              </div>
            {%- endif %}
          {% endblock %}

      {%- if render_sidebar %}
        </div>
      {%- endif %}
      </div>
    {%- endblock %}
    <div class="clearer"></div>
  </div>
{%- else %}
{{ super() }}
{%- endif %}
{%- endblock %}
```

- It extends basic/layout.html <!-- .element: class="fragment"  data-code-focus="1" -->
- It fills the content block <!-- .element: class="fragment" data-code-focus="43" -->
- By default, gets sidebar from super() <!-- .element: class="fragment" data-code-focus="82" --> 

----

### ``basic/layout.html``

```html+jinja 
{#
    basic/layout.html
    ~~~~~~~~~~~~~~~~~

    Master layout template for Sphinx themes.

    :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
#}
{%- block doctype -%}{%- if html5_doctype %}
<!DOCTYPE html>
{%- else %}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
{%- endif %}{%- endblock %}
{%- set reldelim1 = reldelim1 is not defined and ' &#187;' or reldelim1 %}
{%- set reldelim2 = reldelim2 is not defined and ' |' or reldelim2 %}
{%- set render_sidebar = (not embedded) and (not theme_nosidebar|tobool) and
                         (sidebars != []) %}
{%- set url_root = pathto('', 1) %}
{# XXX necessary? #}
{%- if url_root == '#' %}{% set url_root = '' %}{% endif %}
{%- if not embedded and docstitle %}
  {%- set titlesuffix = " &#8212; "|safe + docstitle|e %}
{%- else %}
  {%- set titlesuffix = "" %}
{%- endif %}

{%- macro relbar() %}
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>{{ _('Navigation') }}</h3>
      <ul>
        {%- for rellink in rellinks %}
        <li class="right" {% if loop.first %}style="margin-right: 10px"{% endif %}>
          <a href="{{ pathto(rellink[0]) }}" title="{{ rellink[1]|striptags|e }}"
             {{ accesskey(rellink[2]) }}>{{ rellink[3] }}</a>
          {%- if not loop.first %}{{ reldelim2 }}{% endif %}</li>
        {%- endfor %}
        {%- block rootrellink %}
        <li class="nav-item nav-item-0"><a href="{{ pathto(master_doc) }}">{{ shorttitle|e }}</a>{{ reldelim1 }}</li>
        {%- endblock %}
        {%- for parent in parents %}
          <li class="nav-item nav-item-{{ loop.index }}"><a href="{{ parent.link|e }}" {% if loop.last %}{{ accesskey("U") }}{% endif %}>{{ parent.title }}</a>{{ reldelim1 }}</li>
        {%- endfor %}
        {%- block relbaritems %} {% endblock %}
      </ul>
    </div>
{%- endmacro %}

{%- macro sidebar() %}
      {%- if render_sidebar %}
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
          {%- block sidebarlogo %}
          {%- if logo %}
            <p class="logo"><a href="{{ pathto(master_doc) }}">
              <img class="logo" src="{{ pathto('_static/' + logo, 1) }}" alt="Logo"/>
            </a></p>
          {%- endif %}
          {%- endblock %}
          {%- if sidebars != None %}
            {#- new style sidebar: explicitly include/exclude templates #}
            {%- for sidebartemplate in sidebars %}
            {%- include sidebartemplate %}
            {%- endfor %}
          {%- else %}
            {#- old style sidebars: using blocks -- should be deprecated #}
            {%- block sidebartoc %}
            {%- include "localtoc.html" %}
            {%- endblock %}
            {%- block sidebarrel %}
            {%- include "relations.html" %}
            {%- endblock %}
            {%- block sidebarsourcelink %}
            {%- include "sourcelink.html" %}
            {%- endblock %}
            {%- if customsidebar %}
            {%- include customsidebar %}
            {%- endif %}
            {%- block sidebarsearch %}
            {%- include "searchbox.html" %}
            {%- endblock %}
          {%- endif %}
        </div>
      </div>
      {%- endif %}
{%- endmacro %}

{%- macro script() %}
    <script type="text/javascript" id="documentation_options" data-url_root="{{ pathto('', 1) }}" src="{{ pathto('_static/documentation_options.js', 1) }}"></script>
    {%- for scriptfile in script_files %}
    <script type="text/javascript" src="{{ pathto(scriptfile, 1) }}"></script>
    {%- endfor %}
{%- endmacro %}

{%- macro css() %}
    <link rel="stylesheet" href="{{ pathto('_static/' + style, 1) }}" type="text/css" />
    <link rel="stylesheet" href="{{ pathto('_static/pygments.css', 1) }}" type="text/css" />
    {%- for css in css_files %}
      {%- if css|attr("rel") %}
    <link rel="{{ css.rel }}" href="{{ pathto(css.filename, 1) }}" type="text/css"{% if css.title is not none %} title="{{ css.title }}"{% endif %} />
      {%- else %}
    <link rel="stylesheet" href="{{ pathto(css, 1) }}" type="text/css" />
      {%- endif %}
    {%- endfor %}
{%- endmacro %}

{%- if html_tag %}
{{ html_tag }}
{%- else %}
<html xmlns="http://www.w3.org/1999/xhtml"{% if language is not none %} lang="{{ language }}"{% endif %}>
{%- endif %}
  <head>
    {%- if not html5_doctype and not skip_ua_compatible %}
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    {%- endif %}
    {%- if use_meta_charset or html5_doctype %}
    <meta charset="{{ encoding }}" />
    {%- else %}
    <meta http-equiv="Content-Type" content="text/html; charset={{ encoding }}" />
    {%- endif %}
    {{- metatags }}
    {%- block htmltitle %}
    <title>{{ title|striptags|e }}{{ titlesuffix }}</title>
    {%- endblock %}
    {%- block css %}
    {{- css() }}
    {%- endblock %}
    {%- if not embedded %}
    {%- block scripts %}
    {{- script() }}
    {%- endblock %}
    {%- if use_opensearch %}
    <link rel="search" type="application/opensearchdescription+xml"
          title="{% trans docstitle=docstitle|e %}Search within {{ docstitle }}{% endtrans %}"
          href="{{ pathto('_static/opensearch.xml', 1) }}"/>
    {%- endif %}
    {%- if favicon %}
    <link rel="shortcut icon" href="{{ pathto('_static/' + favicon, 1) }}"/>
    {%- endif %}
    {%- endif %}
{%- block linktags %}
    {%- if hasdoc('about') %}
    <link rel="author" title="{{ _('About these documents') }}" href="{{ pathto('about') }}" />
    {%- endif %}
    {%- if hasdoc('genindex') %}
    <link rel="index" title="{{ _('Index') }}" href="{{ pathto('genindex') }}" />
    {%- endif %}
    {%- if hasdoc('search') %}
    <link rel="search" title="{{ _('Search') }}" href="{{ pathto('search') }}" />
    {%- endif %}
    {%- if hasdoc('copyright') %}
    <link rel="copyright" title="{{ _('Copyright') }}" href="{{ pathto('copyright') }}" />
    {%- endif %}
    {%- if next %}
    <link rel="next" title="{{ next.title|striptags|e }}" href="{{ next.link|e }}" />
    {%- endif %}
    {%- if prev %}
    <link rel="prev" title="{{ prev.title|striptags|e }}" href="{{ prev.link|e }}" />
    {%- endif %}
{%- endblock %}
{%- block extrahead %} {% endblock %}
  </head>
  {%- block body_tag %}<body>{% endblock %}
{%- block header %}{% endblock %}

{%- block relbar1 %}{{ relbar() }}{% endblock %}

{%- block content %}
  {%- block sidebar1 %} {# possible location for sidebar #} {% endblock %}

    <div class="document">
  {%- block document %}
      <div class="documentwrapper">
      {%- if render_sidebar %}
        <div class="bodywrapper">
      {%- endif %}
          <div class="body" role="main">
            {% block body %} {% endblock %}
          </div>
      {%- if render_sidebar %}
        </div>
      {%- endif %}
      </div>
  {%- endblock %}

  {%- block sidebar2 %}{{ sidebar() }}{% endblock %}
      <div class="clearer"></div>
    </div>
{%- endblock %}

{%- block relbar2 %}{{ relbar() }}{% endblock %}

{%- block footer %}
    <div class="footer" role="contentinfo">
    {%- if show_copyright %}
      {%- if hasdoc('copyright') %}
        {% trans path=pathto('copyright'), copyright=copyright|e %}&#169; <a href="{{ path }}">Copyright</a> {{ copyright }}.{% endtrans %}
      {%- else %}
        {% trans copyright=copyright|e %}&#169; Copyright {{ copyright }}.{% endtrans %}
      {%- endif %}
    {%- endif %}
    {%- if last_updated %}
      {% trans last_updated=last_updated|e %}Last updated on {{ last_updated }}.{% endtrans %}
    {%- endif %}
    {%- if show_sphinx %}
      {% trans sphinx_version=sphinx_version|e %}Created using <a href="http://sphinx-doc.org/">Sphinx</a> {{ sphinx_version }}.{% endtrans %}
    {%- endif %}
    </div>
{%- endblock %}
  </body>
</html>
```

- Content block calls sidebar macro <!-- .element: class="fragment"  data-code-focus="187" -->
- The sidebar macro... <!-- .element: class="fragment" data-code-focus="50" -->
- ...has newstyle, loops through sidebars <!-- .element: class="fragment" data-code-focus="63" --> 



----

## Sidebars?

TODO giphy of wtf

----

### Magic variable from ``html_theme_options``

TODO Screenshot of sphinx html theming page http://www.sphinx-doc.org/en/stable/config.html#confval-html_sidebars

- Circle "relations.html"

----

## ``_templates/relations.html``

TODO include source which has my stuff and calls super

- Override the layer-layer

----

## Results in...

TODO screenshot

----

## Aside: Magic

TODO Picture of wizard blowing up in face: As Uncle Timmy always said...explicit is better than implicit"

- A brief taste of the layers of magic
- Template blocks/macros/layouts, layers, theme conf
- Vast ecosystem of informal, inconsistent, implicit conventions

----  ----

### 2b. Add some CSS

I'd like to style that my-addition in the sidebar.

----

### Solution? Magical Magic!

TODO Screenshot of http://www.sphinx-doc.org/en/stable/config.html#confval-html_static_path

----

### ``_static/mystyles.css``

TODO Inline the CSS

----

### Edit ``conf.py``

TODO Inline the conf.py setting

----

### Et voilà

TODO Screenshot of styled box

----

### Dynamic CSS?

- Sure, why not
- ``_static/mystyles.css_t``
- Becomes a Jinja2 template

----  ----


### 2c. Install a new extension

Let's change to a Bootstrap theme.


----

### Install package

TODO fenced block for pip

----

### Configure in ``conf.py``

TODO fenced block for conf.py

- Fragment for extensions
- Fragment for connect as theme
- Fragment for configure some options

----

### Your Sphinx looks different

TODO screenshot of new site


----  ----


### 2d. Other Extensions

- New directive
- New builders
- Your own crazy thing

----  ----

## 3. Hard: Extending

----  ----


### What is an extension?

- Package with a __init__.setup() function that gets passed app
- Registers new kinds of things
- Listens for for events

----

### Example: Alabaster

TODO fenced block for setup()


----

### Todo example

TODO hyperlink and screenshot of Sphinx todo page

---- ----

### Let's write an extension

Hello World directive. Of course.

----

### ``customizing_sphinx/helloworld.py``

TODO code block of directive

----

### ``customizing_sphinx/__init__.py``

TODO code block of setup.py

----

### Add it to ``conf.py``

TODO code block of conf.py

----

### We now have a new directive...

TODO Show an RST document

----

### ...which renders in a page

TODO Screenshot of helloworld

----

### Wrong usage, and...

TODO code of rst without argument

----

### ...Sphinx warns us

TODO bash output of running sphinx with error

----

### Don't be stupid, write tests

- The cycle of code, run Sphinx, look at browser...sucks.

- Sphinx has a pytest fixture

---- 

### ``tests/confdir.py``

TODO Code for fixture

---- 

#### tests/test_helloworld.py

TODO code snippet for test

---- ----

## Any Questions?

TODO giphy of Just Kidding

- I know, that was a lot, but...
- URL to repo

----  ----

### Conclusion

- Sphinx is big, powerful, old, crazy
- Under-appreciated as Python's secret weapon
- Contact me: hallway, sprint, open space, @paulweveritt 

