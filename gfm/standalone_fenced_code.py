# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import markdown

from markdown.extensions.fenced_code import FencedCodeExtension, FencedBlockPreprocessor


class StandaloneFencedCodeExtension(FencedCodeExtension):
    def __init__(self, **kwargs):
        self.config = {
            "linenums": [False, "Use lines numbers. True=yes, False=no, None=auto"],
            "guess_lang": [False, "Automatic language detection - Default: True"],
            "css_class": [
                "highlight",
                "Set class name for wrapper <div> - " "Default: codehilite",
            ],
            "pygments_style": [
                "default",
                "Pygments HTML Formatter Style " "(Colorscheme) - Default: default",
            ],
            "noclasses": [
                False,
                "Use inline styles instead of CSS classes - " "Default false",
            ],
            "use_pygments": [
                True,
                "Use Pygments to Highlight code blocks. "
                "Disable if using a JavaScript library. "
                "Default: True",
            ],
        }
        # Markdown 3.3 introduced a breaking change.
        if markdown.__version_info__ >= (3, 3):
            super().setConfigs(kwargs)
        else:
            super().__init__(**kwargs)

    def extendMarkdown(self, md):
        """Add FencedBlockPreprocessor to the Markdown instance."""
        md.registerExtension(self)
        # Markdown 3.3 introduced a breaking change.
        if markdown.__version_info__ >= (3, 3):
            processor = FencedBlockPreprocessor(md, self.config)
            processor.codehilite_conf = self.getConfigs()
        else:
            processor = FencedBlockPreprocessor(md)
            processor.checked_for_codehilite = True
            processor.codehilite_conf = self.config
        md.preprocessors.register(processor, "fenced_code_block", 25)
