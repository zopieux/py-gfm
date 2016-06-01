# coding: utf-8
# Copyright (c) 2013, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from __future__ import unicode_literals

import gfm
from test_case import TestCase


class TestTaskList(TestCase):
    def setUp(self):
        def cb_attrs(parent, li):
            return {'data-foo': li.text.split('=')[1]}

        def list_attrs(list, depth):
            return {'data-tag': list.tag, 'data-depth': str(depth)}

        self.tasklist = gfm.TaskListExtension()
        self.tasklist_ordered_disabled = gfm.TaskListExtension(ordered=False)
        self.tasklist_full_disabled = gfm.TaskListExtension(ordered=False, unordered=False)
        self.tasklist_no_marker = gfm.TaskListExtension(checked=[], unchecked=[])
        self.tasklist_patterns = gfm.TaskListExtension(checked=['~o', '[o]'],
                                                       unchecked=('~', '[ ]'))
        self.tasklist_max_depth = gfm.TaskListExtension(max_depth=2)
        self.tasklist_item_attrs = gfm.TaskListExtension(
            item_attrs={'class': 'foo'})
        self.tasklist_box_attrs = gfm.TaskListExtension(
            checkbox_attrs={'name': 'foo'})
        self.tasklist_box_attrs_cb = gfm.TaskListExtension(
            checkbox_attrs=cb_attrs)
        self.tasklist_list_attrs = gfm.TaskListExtension(
            list_attrs={'class': 'somelist'})
        self.tasklist_list_attrs_cb = gfm.TaskListExtension(
            list_attrs=list_attrs)

    def test_tasklist_nolist(self):
        self.assert_renders("""
        <p>Text</p>
        <ul>
        <li>first item</li>
        </ul>
        """, """
        Text

        - first item
        """, [self.tasklist])

    def test_tasklist_full_disabled(self):
        self.assert_renders("""
        <ul>
        <li>[ ] first item</li>
        <li>[x] second item</li>
        </ul>
        <p>foo</p>
        <ol>
        <li>[ ] first item</li>
        <li>[x] second item</li>
        </ol>
        """, """
        - [ ] first item
        - [x] second item

        foo

        1. [ ] first item
        1. [x] second item
        """, [self.tasklist_full_disabled])

    def test_tasklist_empty(self):
        self.assert_renders("""
        <ul>
        <li>[ ] first item</li>
        <li>[x] second item</li>
        </ul>
        """, """
        - [ ] first item
        - [x] second item
        """, [self.tasklist_no_marker])

    def test_tasklist_defaults(self):
        self.assert_renders("""
        <ul>
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li>item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        </ul>
        """, """
        - [x] yes item
        - item
        - [ ] no item
        """, [self.tasklist])

    def test_tasklist_ordered_list(self):
        self.assert_renders("""
        <ol>
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li>item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        </ol>
        """, """
        1. [x] yes item
        1. item
        1. [ ] no item
        """, [self.tasklist])

    def test_tasklist_whitespace(self):
        self.assert_renders("""
        <p>-[ ]not a list</p>
        <ul>
        <li><input disabled="disabled" type="checkbox" />item</li>
        <li><input disabled="disabled" type="checkbox" /> item</li>
        <li><input disabled="disabled" type="checkbox" />  item</li>
        </ul>
        """, """
        -[ ]not a list

        - [ ]item
        -  [ ] item
        -   [ ]  item
        """, [self.tasklist])

    def test_tasklist_disabled(self):
        self.assert_renders("""
        <ul>
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        </ul>
        """, """
        - [x] yes item
        - [ ] no item
        """, [self.tasklist_ordered_disabled])
        self.assert_renders("""
        <ol>
        <li>[x] yes item</li>
        <li>[ ] no item</li>
        </ol>
        """, """
        1. [x] yes item
        1. [ ] no item
        """, [self.tasklist_ordered_disabled])

    def test_tasklist_nested(self):
        self.assert_renders("""
        <ul>
        <li><input disabled="disabled" type="checkbox" /> item<ul>
        <li><input disabled="disabled" type="checkbox" /> nested</li>
        <li><input disabled="disabled" type="checkbox" /> nested<ul>
        <li><input disabled="disabled" type="checkbox" /> super nested</li>
        </ul>
        </li>
        </ul>
        </li>
        </ul>
        """, """
        - [ ] item
            - [ ] nested
            - [ ] nested
                - [ ] super nested
        """, [self.tasklist])

    def test_tasklist_custom_patterns(self):
        self.assert_renders("""
        <ul>
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        <li>[x] item</li>
        <li>item</li>
        </ul>
        """, """
        - [o] yes item
        - ~o yes item
        - [ ] no item
        - ~ no item
        - [x] item
        - item
        """, [self.tasklist_patterns])

    def test_tasklist_max_depth(self):
        self.assert_renders("""
        <ul>
        <li><input disabled="disabled" type="checkbox" /> item<ul>
        <li><input disabled="disabled" type="checkbox" /> nested 1<ul>
        <li>[ ] super nested 1</li>
        </ul>
        </li>
        <li><input disabled="disabled" type="checkbox" /> nested 2<ul>
        <li>[ ] super nested 2</li>
        </ul>
        </li>
        </ul>
        </li>
        </ul>
        """, """
        - [ ] item
            - [ ] nested 1
                - [ ] super nested 1
            - [ ] nested 2
                - [ ] super nested 2
        """, [self.tasklist_max_depth])

    def test_tasklist_item_attrs(self):
        self.assert_renders("""
        <ul>
        <li class="foo"><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li class="foo"><input disabled="disabled" type="checkbox" /> no item</li>
        </ul>
        """, """
        - [x] yes item
        - [ ] no item
        """, [self.tasklist_item_attrs])

    def test_tasklist_box_attrs(self):
        self.assert_renders("""
        <ul>
        <li><input checked="checked" disabled="disabled" name="foo" type="checkbox" /> yes item</li>
        <li><input disabled="disabled" name="foo" type="checkbox" /> no item</li>
        </ul>
        """, """
        - [x] yes item
        - [ ] no item
        """, [self.tasklist_box_attrs])

    def test_tasklist_box_attrs_cb(self):
        self.assert_renders("""
        <ul>
        <li><input checked="checked" data-foo="42" disabled="disabled" type="checkbox" /> foo =42</li>
        <li><input data-foo="1337" disabled="disabled" type="checkbox" /> foo =1337</li>
        </ul>
        """, """
        - [x] foo =42
        - [ ] foo =1337
        """, [self.tasklist_box_attrs_cb])

    def test_tasklist_list_attrs(self):
        self.assert_renders("""
        <ul class="somelist">
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        </ul>
        """, """
        - [x] yes item
        - [ ] no item
        """, [self.tasklist_list_attrs])

        # Non-tasklists are not modified
        self.assert_renders("""
        <ul>
        <li>foo</li>
        <li>bar</li>
        </ul>
        """, """
        - foo
        - bar
        """, [self.tasklist_list_attrs])

    def test_tasklist_list_attrs_nested(self):
        self.assert_renders("""
        <ul data-depth="1" data-tag="ul">
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li><input disabled="disabled" type="checkbox" /> no item<ul data-depth="2" data-tag="ul">
        <li><input disabled="disabled" type="checkbox" /> nest 1</li>
        <li><input disabled="disabled" type="checkbox" /> nest 2</li>
        </ul>
        </li>
        </ul>
        """, """
        - [x] yes item
        - [ ] no item
            - [ ] nest 1
            - [ ] nest 2
        """, [self.tasklist_list_attrs_cb])

    def test_tasklist_list_attrs_cb(self):
        self.assert_renders("""
        <ul data-depth="1" data-tag="ul">
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        </ul>
        """, """
        - [x] yes item
        - [ ] no item
        """, [self.tasklist_list_attrs_cb])
        self.assert_renders("""
        <ol data-depth="1" data-tag="ol">
        <li><input checked="checked" disabled="disabled" type="checkbox" /> yes item</li>
        <li><input disabled="disabled" type="checkbox" /> no item</li>
        </ol>
        """, """
        1. [x] yes item
        1. [ ] no item
        """, [self.tasklist_list_attrs_cb])
