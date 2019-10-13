# coding: utf-8
# Copyright (c) 2013, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

"""
:mod:`gfm.spaced_link` -- Links with optional whitespace
========================================================

The :mod:`gfm.spaced_link` module provides an extension that supports links and
images with additional whitespace.

GitHub's Markdown engine allows links and images to have whitespace --
including a single newline -- between the first set of brackets and the
second (e.g. ``[text] (href)``). This extension adds such support.

Typical usage
-------------

.. testcode::

   import markdown
   from gfm import SpacedLinkExtension

   print(markdown.markdown("Check out [this link] (http://example.org/)!",
                           extensions=[SpacedLinkExtension()]))

.. testoutput::

   <p>Check out <a href="http://example.org/">this link</a>!</p>

"""

from __future__ import unicode_literals

import markdown

#BRK = markdown.inlinepatterns.BRK
NOIMG = markdown.inlinepatterns.NOIMG
SPACE = r'(?:\s*(?:\r\n|\r|\n)?\s*)'

#SPACED_LINK_RE = markdown.inlinepatterns.LINK_RE.replace(
#    NOIMG + BRK, NOIMG + BRK + SPACE)
#SPACED_LINK_RE = markdown.inlinepatterns.LINK_RE
SPACED_LINK_RE = r"\[.+\]\s+\(.+\)"

#SPACED_REFERENCE_RE = markdown.inlinepatterns.REFERENCE_RE.replace(
#    NOIMG + BRK, NOIMG + BRK + SPACE)
SPACED_REFERENCE_RE = markdown.inlinepatterns.REFERENCE_RE

#SPACED_IMAGE_LINK_RE = markdown.inlinepatterns.IMAGE_LINK_RE.replace(
#    r'\!' + BRK, r'\!' + BRK + SPACE)
SPACED_IMAGE_LINK_RE = markdown.inlinepatterns.IMAGE_LINK_RE

#SPACED_IMAGE_REFERENCE_RE = markdown.inlinepatterns.IMAGE_REFERENCE_RE.replace(
#    r'\!' + BRK, r'\!' + BRK + SPACE)
SPACED_IMAGE_REFERENCE_RE = markdown.inlinepatterns.IMAGE_REFERENCE_RE


from markdown.inlinepatterns import LinkInlineProcessor, ImageInlineProcessor, ReferenceInlineProcessor, ImageReferenceInlineProcessor, LINK_RE, IMAGE_LINK_RE
import re
class SpacedLinkInlineProcessor(LinkInlineProcessor):
    """ Return a link element from the given match. """
    RE_LINK = re.compile(r'''\s+\(\s*(?:(<[^<>]*>)\s*(?:('[^']*'|"[^"]*")\s*)?\))?''', re.DOTALL | re.UNICODE)
    
class SpacedImageInlineProcessor(ImageInlineProcessor):
    """ Return a link element from the given match. """
    RE_LINK = re.compile(r'''\s+\(\s*(?:(<[^<>]*>)\s*(?:('[^']*'|"[^"]*")\s*)?\))?''', re.DOTALL | re.UNICODE)

    
class SpacedReferenceInlineProcessor(ReferenceInlineProcessor):
    """ Return a link element from the given match. """
    RE_LINK = re.compile(r'\s+\[([^\]]*)\]', re.DOTALL | re.UNICODE)
class SpacedImageReferenceInlineProcessor(ImageReferenceInlineProcessor):
    RE_LINK = re.compile(r'\s+\[([^\]]*)\]', re.DOTALL | re.UNICODE)

class SpacedLinkExtension(markdown.Extension):
    """
    An extension that supports links and images with additional whitespace.
    """

    def extendMarkdown(self, md, md_globals):
        # md.inlinePatterns['link'] = \
        #     markdown.inlinepatterns.LinkPattern(SPACED_LINK_RE, md)
        # md.inlinePatterns['reference'] = \
        #     markdown.inlinepatterns.ReferencePattern(SPACED_REFERENCE_RE, md)
        # md.inlinePatterns['image_link'] = \
        #     markdown.inlinepatterns.ImagePattern(SPACED_IMAGE_LINK_RE, md)
        # md.inlinePatterns['image_reference'] = \
        #     markdown.inlinepatterns.ImageReferencePattern(
        #         SPACED_IMAGE_REFERENCE_RE, md)

        md.inlinePatterns.register(SpacedLinkInlineProcessor(LINK_RE, md), 'spaced_link', 500)
        
        md.inlinePatterns.register(SpacedImageInlineProcessor(IMAGE_LINK_RE, md), 'img_spaced_link', 501)
        
        md.inlinePatterns.register(SpacedReferenceInlineProcessor(LINK_RE, md), 'spaced_reference', 502)
        
        md.inlinePatterns.register(SpacedImageReferenceInlineProcessor(IMAGE_LINK_RE, md), 'img_spaced_reference', 503)
        
        #md.inlinePatterns.register(SpacedLinkInlineProcessor(LINK_RE, md), 'spaced_link', 502)
        # md.inlinePatterns['link'] = \
        #     markdown.inlinepatterns.LinkPattern(SPACED_LINK_RE, md)
        # print(md.inlinePatterns['link'])
        
        # md.inlinePatterns['reference'] = \
        #     markdown.inlinepatterns.ReferencePattern(SPACED_REFERENCE_RE, md)
        # md.inlinePatterns['image_link'] = \
        #     markdown.inlinepatterns.ImagePattern(SPACED_IMAGE_LINK_RE, md)
        # md.inlinePatterns['image_reference'] = \
        #     markdown.inlinepatterns.ImageReferencePattern(
        #         SPACED_IMAGE_REFERENCE_RE, md)

def makeExtension(**kwargs):  # pragma: no cover
    return SpacedLinkExtension(**kwargs)
