# coding: utf-8
# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

"""
:mod:`gfm.hidden_hilite` -- Fenced code blocks with no highlighting
====================================================================

The :mod:`gfm.hidden_hilite` module provides an extension that allows the use
of fenced code blocks without adding syntax highlighting or line numbers.

Typical usage
-------------

.. testcode::

   import markdown
   from gfm import HiddenHiliteExtension

   print(markdown.markdown("```\\nimport this\\nprint('foo')\\n```",
                           extensions=[HiddenHiliteExtension()]))

.. testoutput::

   <p><code>import this
   print('foo')</code></p>

"""

from markdown.extensions.codehilite import CodeHiliteExtension, CodeHilite


class HiddenHiliteExtension(CodeHiliteExtension):
    """
    A subclass of CodeHiliteExtension that doesn't highlight on its own.
    """

try:
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name, guess_lexer
    from pygments.formatters import get_formatter_by_name
    pygments = True
except ImportError:
    pygments = False

class HiddenHiliteExtension(CodeHiliteExtension):
    """
    A subclass of CodeHiliteExtension that doesn't highlight on its own.
    """
    
    # def __init__(self, **kwargs):
    #     # define default configs
    #     self.config = {
    #         'linenums': [None,
    #                      "Use lines numbers. True=yes, False=no, None=auto"],
    #         'guess_lang': [True,
    #                        "Automatic language detection - Default: True"],
    #         'css_class': ["codehilite",
    #                       "Set class name for wrapper <div> - "
    #                       "Default: codehilite"],
    #         'pygments_style': ['default',
    #                            'Pygments HTML Formatter Style '
    #                            '(Colorscheme) - Default: default'],
    #         'noclasses': [False,
    #                       'Use inline styles instead of CSS classes - '
    #                       'Default false'],
    #         'use_pygments': [True,
    #                          'Use Pygments to Highlight code blocks. '
    #                          'Disable if using a JavaScript library. '
    #                          'Default: True']
    #         }
    #     super(HiddenHiliteExtension, self).__init__(**kwargs)
        
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        for key in self.config:
            if key in md_globals:
                self.config[key][0] = md_globals[key][0]
        

class HiddenHilite(CodeHilite):
    def __init__(self, *_, **args4base):
        if _:
            raise TypeError("__init__() expected a keyword argument only")
        
        CodeHilite.__init__(self,**args4base)

    def hilite(self):
        return CodeHilite.hilite(self)
