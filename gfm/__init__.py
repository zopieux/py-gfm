# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

"""
:mod:`gfm` -- Base module for GitHub-Flavored Markdown
======================================================
"""

from gfm import autolink
from gfm import automail
from gfm import standalone_fenced_code
from gfm import semi_sane_lists
from gfm import strikethrough
from gfm import tasklist

AutolinkExtension = autolink.AutolinkExtension
AutomailExtension = automail.AutomailExtension
StandaloneFencedCodeExtension = standalone_fenced_code.StandaloneFencedCodeExtension
SemiSaneListExtension = semi_sane_lists.SemiSaneListExtension
StrikethroughExtension = strikethrough.StrikethroughExtension
TaskListExtension = tasklist.TaskListExtension

__all__ = [
    "AutolinkExtension",
    "AutomailExtension",
    "SemiSaneListExtension",
    "StandaloneFencedCodeExtension",
    "StrikethroughExtension",
    "TaskListExtension",
]
