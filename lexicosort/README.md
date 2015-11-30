Lexical Sort
============

This module can either be called from the command line or used
as an import in other Python code. To see examples and
instructions for command line use, call it with `--help`. The
arguments to use if importing this module are explained in the
docstring.

Runtime Analysis
----------------
This is just using Python's built-in Timsort directly. If the
strings are exceptionally long, perhaps the translation and
comparison will outweigh the sort time, but this is unlikely.

Python's string compares are O(m) where m is the length of the
string (from https://docs.python.org/2/reference/expressions.html#not-in).

Timsort is O(n * log(n)) where n is the number of elements to be sorted
(from https://en.wikipedia.org/wiki/Timsort#Analysis).
