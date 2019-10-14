# coding: utf-8
# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

"""
:mod:`gfm` -- Base module for GitHub-Flavored Markdown
======================================================
"""

from gfm import autolink
from gfm import automail
from gfm import hidden_hilite
from gfm import semi_sane_lists
from gfm import spaced_link
from gfm import strikethrough
from gfm import tasklist

AutolinkExtension = autolink.AutolinkExtension
AutomailExtension = automail.AutomailExtension
HiddenHiliteExtension = hidden_hilite.HiddenHiliteExtension
SemiSaneListExtension = semi_sane_lists.SemiSaneListExtension
SpacedLinkExtension = spaced_link.SpacedLinkExtension
StrikethroughExtension = strikethrough.StrikethroughExtension
TaskListExtension = tasklist.TaskListExtension

__all__ = ['AutolinkExtension', 'AutomailExtension', 'HiddenHiliteExtension',
           'SemiSaneListExtension', 'SpacedLinkExtension',
           'StrikethroughExtension', 'TaskListExtension']



from mdx_partial_gfm import PartialGithubFlavoredMarkdownExtension
from markdown.extensions.nl2br import Nl2BrExtension

def makeExtension(*args, **kwargs):
    return GithubFlavoredMarkdownExtension(*args, **kwargs)


class GithubFlavoredMarkdownExtension(PartialGithubFlavoredMarkdownExtension):
    """
    An extension that is as compatible as possible with GitHub-flavored
    Markdown (GFM).

    This extension aims to be compatible with the standard GFM that GitHub uses
    for comments and issues. It has all the extensions described in the `GFM
    documentation`_, except for intra-GitHub links to commits, repositories,
    and issues.

    Note that Markdown-formatted gists and files (including READMEs) on GitHub
    use a slightly different variant of GFM. For that, use
    :class:`mdx_partial_gfm.PartialGithubFlavoredMarkdownExtension`.

    .. _GFM documentation: https://guides.github.com/features/mastering-markdown/
    """
    config = {
        'linenums': [None,
                     "Use lines numbers. True=yes, False=no, None=auto"],
        'guess_lang': [True,
                       "Automatic language detection - Default: True"],
        'css_class': ["highlight",
                      "Set class name for wrapper <div> - "
                      "Default: codehilite"],
        'pygments_style': ['default',
                           'Pygments HTML Formatter Style '
                           '(Colorscheme) - Default: default'],
        'noclasses': [False,
                      'Use inline styles instead of CSS classes - '
                      'Default false'],
        'use_pygments': [True,
                         'Use Pygments to Highlight code blocks. '
                         'Disable if using a JavaScript library. '
                         'Default: True'],
        'pygments_show_filename': [False,
                         'Show gfm styled filename for codeblock'
                         'Default: False'],
        }
    def extendMarkdown(self, md, md_globals):
        PartialGithubFlavoredMarkdownExtension.extendMarkdown(self, md,
                                                              md_globals)
        #Nl2BrExtension().extendMarkdown(md, md_globals)
        Nl2BrExtension().extendMarkdown(md)
