# Customizing Sphinx

### Simple, Normal, Hard

Paul Everitt, @paulweveritt

----  ----

## Intro

- 5 min
- whoami
- set the scene

----  ----

## Simple: Configuration

- 5 min
- Change some values
- Change some theme options

----

### Change Some Values

----

### Change some theme options


----  ----

## Normal: Customizing

- 10 min

----

### Override a template

- The Sphinx "basic" template structure

----

### Add some CSS

----

### Add some images


----

### Install a new extension

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

