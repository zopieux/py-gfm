# GitHub-Flavored Markdown for Python

[![Build status](https://travis-ci.org/Zopieux/py-gfm.svg?branch=master)](https://travis-ci.org/Zopieux/py-gfm)

This is an implementation of [GitHub-Flavored Markdown][gfm] written as an
extension to the Python [Markdown][md] library. It aims for maximal
compatibility with GitHub's rendering.


## Supported features

- Fenced code blocks
- Literal line breaks
- Tables
- Hyperlink parsing (`http`, `https`, `ftp`, `email` and `www` subdomains)
- Code highlighting (dummy, no actual syntactic coloration as-is)
- Mixed-style lists with no separation
- Links and images with whitespace
- Strikethrough
- Task lists


## Unsupported features

This implementation does not support all of GFM features.

### Unsupported by design

- Link to commits, issues, pull requests and user profiles: this is
  application specific. Feel free to subclass the provided classes to
  implement your own logic.

### Unsupported, but planned

- Horizontal rules
- Emojis


## License

BSD-style. See [LICENSE](/LICENSE).

[gfm]: http://github.github.com/github-flavored-markdown/
[md]: http://packages.python.org/Markdown/
