py-gfm documentation
====================

|Build status| |Coverage status| |Documentation status|

This is an implementation of `GitHub-Flavored Markdown`_ written as an
extension to the Python `Markdown`_ library. It aims for maximal
compatibility with GitHub's rendering.

py-gfm code is under a BSD-style :ref:`license <license>`.

Installation
------------

::

   pip install py-gfm

Quick start
-----------

All-in-one extension
~~~~~~~~~~~~~~~~~~~~

::

   import markdown
   from mdx_gfm import GithubFlavoredMarkdownExtension

   source = """
   Hello, *world*! This is a ~~good~~marvelous day!
   Here is an auto link: https://example.org/

   Le me introduce you to [task lists](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

   - [ ] eggs
   - [x] milk

   You can also have fenced code blocks:

   ```
   import this
   ```
   """

   # Direct conversion
   html = markdown.markdown(
       source, extensions=[GithubFlavoredMarkdownExtension()])

   # Factory-like
   md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
   html = md.convert(source)


À la carte
~~~~~~~~~~

::

   import markdown
   from gfm import AutolinkExtension, TaskListExtension

   html = markdown.markdown(
       source, extensions=[AutolinkExtension(),
                           TaskListExtension(max_depth=2)])

Available extensions
--------------------

.. toctree::
   :maxdepth: 1

   lib/index

Modules
-------

.. toctree::
   :titlesonly:

   module/gfm
   module/mdx_gfm
   module/mdx_partial_gfm

Supported features
------------------

-  Fenced code blocks
-  Literal line breaks
-  Tables
-  Hyperlink parsing (``http``, ``https``, ``ftp``, ``email`` and
   ``www`` subdomains)
-  Code highlighting (dummy, no actual syntactic coloration as-is)
-  Mixed-style lists with no separation
-  Strikethrough
-  Task lists

Unsupported features
--------------------

This implementation does not support all of GFM features.

By design
~~~~~~~~~

-  Link to commits, issues, pull requests and user profiles: this is
   application specific. Feel free to subclass the provided classes to
   implement your own logic.

Planned
~~~~~~~

-  Horizontal rules
-  Emojis

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _GitHub-Flavored Markdown: https://github.github.com/github-flavored-markdown/
.. _Markdown: https://pythonhosted.org/Markdown/

.. |Build status| image:: https://github.com/Zopieux/py-gfm/workflows/Test%20with%20coverage,%20package,%20lint/badge.svg
.. |Coverage status| image:: https://coveralls.io/repos/github/Zopieux/py-gfm/badge.svg?branch=master
.. |Documentation status| image:: https://readthedocs.org/projects/py-gfm/badge/?version=latest
