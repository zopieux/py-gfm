# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

"""
:mod:`gfm.automail` -- Turn email addresses into links
======================================================

The :mod:`gfm.automail` module provides an extension that turns all raw email
addresses into marked-up links.

Typical usage
-------------

.. testcode::

   import markdown
   from gfm import AutomailExtension

   print(markdown.markdown("You can mail me at foo@example.org for more info",
                           extensions=[AutomailExtension()]))

.. testoutput::

   <p>You can mail me at <a href="mailto:foo@example.org">foo@example.org</a> for more info</p>

"""

import markdown
import markdown.inlinepatterns
import xml.etree.ElementTree as etree

MAIL_RE = r"\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+)\b"


# We can't re-use the built-in AutomailPattern because we need to add mailto:.
# We also don't care about HTML-encoding the email.
class AutomailPattern(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        el = etree.Element("a")
        el.set("href", self.unescape("mailto:" + m.group(2)))
        el.text = markdown.util.AtomicString(m.group(2))
        return el


class AutomailExtension(markdown.Extension):
    """
    An extension that turns email addresses into links.
    """

    def extendMarkdown(self, md):
        md.inlinePatterns.register(AutomailPattern(MAIL_RE, md), "gfm-automail", 100)
