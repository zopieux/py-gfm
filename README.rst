GitHub-Flavored Markdown for Python
===================================

**PLEASE READ BEFORE USING:**
**This repository will not receive bug fixes, and might become read-only soon.**

Rationale: this library has well-known `consistency issues`_ with GitHub-Flavored Markdown rendering. Fixing
them would require time investment the maintainer cannot provide. The maintainer is also fatigued by
Markdown's library constantly breaking their internal API with each minor release.

**Consider instead using** |pycmarkgfm|_ (PyPi_), a lightweight Python 3.5+ wrapper for GitHub's 
own implementation of GFM from the same author,
which is faster, virtually byte-compatible with GitHub rendering,
and provides a nice API for managing task lists aka. TODO lists.

.. _`consistency issues`: https://github.com/Zopieux/py-gfm/issues?q=is%3Aissue+is%3Aopen+label%3Aconformance
.. _pycmarkgfm: https://github.com/Zopieux/pycmarkgfm
.. |pycmarkgfm| replace:: **pycmarkgfm**
.. _PyPi: https://pypi.org/project/pycmarkgfm/

|Build status| |Coverage status| |Documentation status|

This is an implementation of `GitHub-Flavored Markdown`_ written as an
extension to the Python `Markdown`_ library. It aims for, but does not
achieve, maximal compatibility with GitHub's rendering.

Tested Python versions are 3.5 to 3.8. Sorry, no Python 2.7 support starting
with py-gfm 1.x since the Python Markdown library itself is Python 3 only.

Documentation
-------------

You can browse or download the precompiled documentation
on `Read the Docs`_.

To build the Sphinx documentation from source, use::

   cd doc && make html

Supported features
------------------

-  Fenced code blocks
-  Literal line breaks
-  Tables
-  Hyperlink parsing (``http``, ``https``, ``ftp``, ``email`` and
   ``www`` subdomains)
-  Code highlighting for code blocks if Pygments is available
-  Mixed-style lists with no separation
-  Strikethrough
-  Task lists

Unsupported features and known differences
------------------------------------------

py-gfm is a pure Python implementation based on the Python Markdown library and
therefore cannot reproduce GitHub's `own implementation`_ with 100% accuracy.

See `the docs`_ for a list of known discrepancies.

License
-------

BSD-style. See `LICENSE`_.

.. _GitHub-Flavored Markdown: https://docs.github.com/en/github/writing-on-github
.. _Markdown: https://python-markdown.github.io/
.. _Read the Docs: https://py-gfm.readthedocs.io/
.. _LICENSE: /LICENSE
.. _`the docs`: https://py-gfm.readthedocs.io/#unsupported-features
.. _`own implementation`: https://github.com/github/cmark-gfm

.. |Build status| image:: https://github.com/Zopieux/py-gfm/workflows/Test%20and%20package/badge.svg
   :target: https://github.com/Zopieux/py-gfm/actions?query=workflow%3A%22Test+and+package%22
   :alt: Build status
.. |Coverage status| image:: https://coveralls.io/repos/github/Zopieux/py-gfm/badge.svg?branch=master
   :target: https://coveralls.io/github/Zopieux/py-gfm?branch=master
   :alt: Coverage status
.. |Documentation status| image:: https://readthedocs.org/projects/py-gfm/badge/?version=latest
   :target: https://py-gfm.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status
