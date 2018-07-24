# REVEAL.JS TEMPLATE

## [reveal.js][3] presentation written in [markdown][4] set up with [fabric][5] & [fabsetup][6]

created by [theno](https://github.com/theno) | 2017-01-05 | [online][1] | [src][2]


[1]: https://theno.github.io/revealjs_template
[2]: https://github.com/theno/revealjs_template

[3]: http://lab.hakim.se/reveal-js/
[4]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[5]: http://www.fabfile.org/
[6]: https://github.com/theno/fabsetup



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

