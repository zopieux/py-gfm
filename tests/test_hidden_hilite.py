# coding: utf-8
# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from __future__ import unicode_literals

import gfm
from test_case import TestCase


class TestHiddenHilite(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        #self.hidden_hilite = gfm.HiddenHiliteExtension([])
        self.hidden_hilite = gfm.HiddenHiliteExtension()

    def test_doesnt_highlight_code_blocks(self):
        self.assert_renders("""
        <pre><code>def
        </code></pre>
        """, """
            def
        """, [self.hidden_hilite])

    def test_doesnt_highlight_code_blocks_with_shebangs(self):
        self.assert_renders("""
        <pre><code>#!/bin/python
        def
        </code></pre>
        """, """
            #!/bin/python
            def
        """, [self.hidden_hilite])

    def test_doesnt_highlight_code_blocks_with_colons(self):
        self.assert_renders("""
        <pre><code>:::python
        def
        </code></pre>
        """, """
            :::python
            def
        """, [self.hidden_hilite])

    def test_does_highlight_fenced_blocks(self):
        test_text = """
        ```python
        def
        ```
        """
        #extensions = [self.hidden_hilite, 'fenced_code']
        extensions = [self.hidden_hilite, 'gfm.fenced_code']
        if self.has_pygments:
            self.assert_renders("""
        <div class="codehilite"><pre><span></span><span class="k">def</span>
        </pre></div>
        """, test_text, extensions)
        else:
            self.assert_renders("""
        <pre class="codehilite"><code class="language-python">def</code></pre>
        """, test_text, extensions)
