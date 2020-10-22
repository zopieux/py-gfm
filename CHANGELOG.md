## 1.0.1

* Fix compatibility for Markdown 3.3.1 and up.

## 1.0.0

This major revision **is not backward compatible** and introduces **subtle rendering diffs**.

* Replace Markdown < 3.0 support with Markdown >= 3.0 support.
* Drop support for Python 2 since Markdown >= 3.2 [drops it](https://python-markdown.github.io/change_log/release-3.2/) too.
* Remove support for space links (space between `[text]` and `(url)`) that does not seem to be supported in upstream GFM anymore.
* Refactor code syntax highlighting support. Module `hidden_hilite` is removed. This introduces minor HTML structure changes (new `<code>` tags and different `class=`) for both indented and fenced code blocks.
* *Meta*: continuous integration (CI) for testing is now handled by GitHub Actions instead of Travis.

## 0.1.4

* No feature change.
* Pin Markdown dependency to <3.0, as Markdown 3.0 introduced breaking changes
  to its internal API (issue #13). A future release of py-gfm that is compatible
  with Markdown ≥3.0 is planned, with no ETA.

## 0.1.3

* Task lists: support for list attributes (issues #2, #3)

## 0.1.2

* Support for GitHub-like task lists.

## 0.1.1

* Support Python 3.
