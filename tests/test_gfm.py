# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import markdown

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
            if markdown.__version_info__ >= (3, 3):
                expected_text = """
        <pre class="highlight"><code>some code
        </code></pre>
        """
            else:
                expected_text = """
        <pre class="highlight"><code>some code</code></pre>
        """
            self.assert_renders(
                expected_text, test_text, extensions,
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

        # Markdown 3.3+ introduces a new line. *sigh*
        new_line = ""
        if markdown.__version_info__[:2] >= (3, 3):
            new_line = "\n"

        # Markdown 3.3 adds the language to the class but it's reverted
        # in 3.3.1. *sigh*
        code_class = ""
        if markdown.__version_info__[:3] == (3, 3, 0):
            code_class = "python "

        if self.has_pygments:
            expected_text = """
        <div class="{code_class}highlight"><pre><span></span><code><span class="k">def</span>
        </code></pre></div>
        """
        else:
            expected_text = """
        <pre class="{code_class}highlight"><code class="language-python">def{new_line}</code></pre>
        """

        expected_text = expected_text.format(new_line=new_line, code_class=code_class)
        self.assert_renders(expected_text, test_text, extensions)

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
