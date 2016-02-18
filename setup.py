#!/bin/env python3

from distutils.core import setup, Extension

_suffix_tree = Extension('_suffix_tree', ['python_bindings.c',
                                          'suffix_tree.c'])

setup(name="suffix_tree",
      version="3.0",
      description="""
      A python suffix tree (for easy algorithmic prototyping) with Unicode support.

      This is a Python 3 port of the original work done by:
      Dell Zhang <dell.z@ieee.org>
      Original documentation and reference:
      http://researchonsearch.blogspot.com/2010/05/suffix-tree-implementation-with-unicode.html
      """,

      author="Matt Porritt",     author_email="mattp@catalyst-au.net",
      maintainer="Matt Porritt", maintainer_email="mattp@catalyst-au.net",
      contact="Matt Porritt",    contact_email="mattp@catalyst-au.net",
      url='https://github.com/mattporritt/suffix-tree-unicode',
      license="GNU GPLv3",

      scripts=[],
      py_modules=["suffix_tree"],
      ext_modules=[_suffix_tree],
      )
