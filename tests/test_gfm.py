# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from test_case import TestCase


class TestGfm(TestCase):
    def test_indented_code(self):
        self.assert_renders(
            """
        <p>foo</p>
        <pre><code>some code
        </code></pre>
        <p>bar</p>
        """,
            """
        foo
        
            some code
        
        bar
        """,
            ["mdx_gfm"],
        )

    def test_fenced_code(self):
        test_text = """
        ```
        some code
        ```
        """
        extensions = ["mdx_gfm"]
        if self.has_pygments:
            self.assert_renders(
                """
        <div class="highlight"><pre><span></span><code>some code
        </code></pre></div>
        """,
                test_text,
                extensions,
            )
        else:
            self.assert_renders(
                """
        <pre class="highlight"><code>some code</code></pre>
        """,
                test_text,
                extensions,
            )

    def test_nl2br(self):
        self.assert_renders(
            """
        <p>foo<br />
        bar</p>
        """,
            """
        foo
        bar
        """,
            ["mdx_gfm"],
        )

    def test_smart_emphasis(self):
        self.assert_renders(
            """
        <p>foo__bar__baz</p>
        """,
            """
        foo__bar__baz
        """,
            ["mdx_gfm"],
        )

    def test_table(self):
        self.assert_renders(
            """
        <table>
        <thead>
        <tr>
        <th>First Header</th>
        <th>Second Header</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>Content Cell</td>
        <td>Content Cell</td>
        </tr>
        <tr>
        <td>Content Cell</td>
        <td>Content Cell</td>
        </tr>
        </tbody>
        </table>
        """,
            """
        First Header  | Second Header
        ------------- | -------------
        Content Cell  | Content Cell
        Content Cell  | Content Cell
        """,
            ["mdx_gfm"],
        )

    def test_code_highlighting(self):
        test_text = """
        ```python
        def
        ```
        """
        extensions = ["mdx_gfm"]

        if self.has_pygments:
            self.assert_renders(
                """
        <div class="highlight"><pre><span></span><code><span class="k">def</span>
        </code></pre></div>
        """,
                test_text,
                extensions,
            )
        else:
            self.assert_renders(
                """
        <pre class="highlight"><code class="language-python">def</code></pre>
        """,
                test_text,
                extensions,
            )

    def test_semi_sane_lists(self):
        self.assert_renders(
            """
        <ul>
        <li>foo</li>
        </ul>
        <ol>
        <li>bar</li>
        </ol>
        """,
            """
        * foo

        1. bar
        """,
            ["mdx_gfm"],
        )

    def test_autolink(self):
        self.assert_renders(
            """
        <p><a href="http://foo.com/bar">http://foo.com/bar</a></p>
        """,
            """
        http://foo.com/bar
        """,
            ["mdx_gfm"],
        )

    def test_automail(self):
        self.assert_renders(
            """
        <p><a href="mailto:foo@bar.com">foo@bar.com</a></p>
        """,
            """
        foo@bar.com
        """,
            ["mdx_gfm"],
        )

    def test_strikethrough(self):
        self.assert_renders(
            """
        <p>This is <del>struck</del>.</p>
        """,
            """
        This is ~~struck~~.
        """,
            ["mdx_gfm"],
        )
