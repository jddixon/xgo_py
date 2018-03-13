# xgo_py/xgoy/__init__.py

import sys

__all__ = [  # CONSTANTS
    '__version__', '__version_date__',
    # FUNCTIONS
    'check_counts',
]

__version__ = '0.0.11'
__version_date__ = '2018-03-13'


def check_counts(infiles, outfiles):
    if not infiles:
        print("INTERNAL ERROR: no infiles")
        sys.exit(1)
    if len(infiles) != len(outfiles):
        print("INTERNAL ERROR: " +
              "input count (%d) and output count (%d) differ" % (
                  len(infiles), len(outfiles)))
        sys.exit(1)
