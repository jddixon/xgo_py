#!/usr/bin/python3

# xgo_py/xgo/setup.py

import re
from distutils.core import setup
__version__ = re.search("__version__\s*=\s*'(.*)'",
                        open('src/xgo/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='xgo_py',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      py_modules=[],
      packages=['src/xgo'],
      # following could be in scripts/ subdir
      scripts=['src/ant2xgo', 'src/xgo2ant', 'src/xgo2py', ],
      description='Python implementation of xgo software',
      url='http://jddixon.github.io/xgo_py',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
