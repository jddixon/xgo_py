#!/usr/bin/python3

# xgo_py/xgo/setup.py

import re
from distutils.core import setup
__version__ = re.search("__version__\s*=\s*'(.*)'",
                        open('xgo/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='xgo_py',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      py_modules=[],
      packages=['xgo'],
      # following could be in scripts/ subdir
      scripts=['ant2xgo', 'xgo2ant', 'xgo2py', ],
      # MISSING description
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      )
