# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

"""
:mod:`mdx_partial_gfm` -- Partial extension for GFM (READMEs, wiki)
===================================================================

An extension that is as compatible as possible with GitHub-flavored
Markdown (GFM).

This extension aims to be compatible with the variant of GFM that GitHub
uses for Markdown-formatted gists and files (including READMEs). This
variant seems to have all the extensions described in the `GFM
documentation`_, except:

- Newlines in paragraphs are not transformed into ``br`` tags.
- Intra-GitHub links to commits, repositories, and issues are not
  supported.

If you need support for features specific to GitHub comments and issues,
please use :class:`mdx_gfm.GithubFlavoredMarkdownExtension`.

.. _GFM documentation: https://guides.github.com/features/mastering-markdown/
"""

from markdown.extensions import Extension
from markdown.extensions.tables import TableExtension

import gfm


def makeExtension(**kwargs):
    return PartialGithubFlavoredMarkdownExtension(**kwargs)


class PartialGithubFlavoredMarkdownExtension(Extension):
    """
    An extension that is as compatible as possible with GitHub-flavored
    Markdown (GFM).

    This extension aims to be compatible with the variant of GFM that GitHub
    uses for Markdown-formatted gists and files (including READMEs). This
    variant seems to have all the extensions described in the `GFM
    documentation`_, except:

    - Newlines in paragraphs are not transformed into ``br`` tags.
    - Intra-GitHub links to commits, repositories, and issues are not
      supported.

    If you need support for features specific to GitHub comments and issues,
    please use :class:`mdx_gfm.GithubFlavoredMarkdownExtension`.

    .. _GFM documentation: https://guides.github.com/features/mastering-markdown/
    """

    def extendMarkdown(self, md):
        # Built-in extensions
        TableExtension().extendMarkdown(md)

        # Custom extensions
        gfm.AutolinkExtension().extendMarkdown(md)
        gfm.AutomailExtension().extendMarkdown(md)
        gfm.SemiSaneListExtension().extendMarkdown(md)
        gfm.StandaloneFencedCodeExtension().extendMarkdown(md)
        gfm.StrikethroughExtension().extendMarkdown(md)
        gfm.TaskListExtension().extendMarkdown(md)
