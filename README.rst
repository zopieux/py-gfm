GitHub-Flavored Markdown for Python
===================================

|Build status| |Coverage status| |Documentation status|

This is an implementation of `GitHub-Flavored Markdown`_ written as an
extension to the Python `Markdown`_ library. It aims for maximal
compatibility with GitHub's rendering.

Documentation
-------------

Sphinx documentation is in the ``doc/`` folder. Build it with::

   cd doc && make html

You can browse or download the precompiled documentation
on `Read the Docs`_.

Supported features
------------------

-  Fenced code blocks
-  Literal line breaks
-  Tables
-  Hyperlink parsing (``http``, ``https``, ``ftp``, ``email`` and
   ``www`` subdomains)
-  Code highlighting (dummy, no actual syntactic coloration as-is)
-  Mixed-style lists with no separation
-  Links and images with whitespace
-  Strikethrough
-  Task lists

Unsupported features
--------------------

This implementation does not support all of GFM features.

Unsupported by design
~~~~~~~~~~~~~~~~~~~~~

-  Link to commits, issues, pull requests and user profiles: this is
   application specific. Feel free to subclass the provided classes to
   implement your own logic.

Unsupported, but planned
~~~~~~~~~~~~~~~~~~~~~~~~

-  Horizontal rules
-  Emojis

License
-------

BSD-style. See `LICENSE`_.

.. _GitHub-Flavored Markdown: http://github.github.com/github-flavored-markdown/
.. _Markdown: https://pythonhosted.org/Markdown/
.. _Read the Docs: https://py-gfm.readthedocs.org/
.. _LICENSE: /LICENSE

.. |Build status| image:: https://travis-ci.org/Zopieux/py-gfm.svg?branch=master
   :target: https://travis-ci.org/Zopieux/py-gfm
   :alt: Build status
.. |Coverage status| image:: https://coveralls.io/repos/github/Zopieux/py-gfm/badge.svg?branch=master
   :target: https://coveralls.io/github/Zopieux/py-gfm?branch=master
   :alt: Coverage status
.. |Documentation status| image:: https://readthedocs.org/projects/py-gfm/badge/?version=latest
   :target: https://py-gfm.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status
