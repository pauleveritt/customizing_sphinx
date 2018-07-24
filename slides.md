# Customizing Sphinx

### Simple, Normal, Hard

Paul Everitt, @paulweveritt

----  ----

## Intro

- 5 min
- whoami
- set the scene

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

## Simple: Configuration

- 5 min
- Change some values
- Change some theme options

----

### Change Some Values

- Sphinx is driven by a conf file
- It looks like this
- If your site looks like this
- And I make this change to the conf file
- And re-run Sphinx
- Your site looks like this
- What other things can I change?

----

### Change some theme options

- One of those things I can change: html_theme
- It has options, for example alabaster
- Where are those options?
- So let's say I write this in theme options and rebuild
- My site now looks like this
- But if I do this (invalid option)
- I get this

----  ----

## Normal: Customizing

- 10 min

----

### Override a template

- Here is the "related topics"
- I'd like to put a paragraph above it with <p class="my-addition"
- In alabaster/alabaster/templates I see relations.html
- _templates/relations.html and regenerate
- I get this result
- Here's what layout looks like
- Here's what page looks like


----

## Aside: Magic

- Picture of wizard blowing up in face: As Uncle Timmy always said...explicit is better than implicit"

----

## Sphinx Template/Block Structure

- Where is this defined?
- Lookup templates and static assets in layers
- Screenshot of http://www.sphinx-doc.org/en/master/theming.html
- Diagram

----

### Add some CSS

- I'd like to style that my-addition in the sidebar
- Add a file
- Or, parameterize it with _t (show example)
- Note that you can override built-in with the magic of same name

----

### Install a new extension

Let's change to a Bootstrap theme.


- pip
- Add to extensions
- Connect as theme
- Configure some options

----

### Install content-oriented extensions

- New directive

----

### Things that extensions can add

- Themes
- Directives
- Builders    

----  ----

## Hard: Extending


----

### What is an extension?

- Package with a __init__.setup() function that gets passed app
- Registers new kinds of things
- Listens for for events

----

### Example: the theme we installed


----

### Todo example


----

### Don't be stupid, write tests

----  ----

### Conclusion

- Sphinx is big, powerful, old, crazy
- Under-appreciated as Python's secret weapon
- Contact me: hallway, sprint, open space, @paulweveritt 

----  ----

### Dependencies

```js
Reveal.initialize({
// Include other options…
dependencies: [
  // Include other dependencies…
  { src: 'path/to/highlight.js' },
  {
    src: 'node_modules/reveal-code-focus/reveal-code-focus.js',
    async: true,
    callback: function() {
      RevealCodeFocus();
    }
  }
]
});
```
<span class="fragment" data-code-focus="5">Note that the `highlight.js` file mentioned is not the [Reveal.js plugin](https://github.com/hakimel/reveal.js/blob/master/plugin/highlight/highlight.js), but the actual [`highlight.js` library](https://highlightjs.org/).</span>
 

----  ----

### Next

Here

