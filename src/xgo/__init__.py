# xgo_py/xgoy/__init__.py

import sys

__all__ = [  # CONSTANTS
    '__version__', '__version_date__',
    # FUNCTIONS
    'checkCounts',
]

__version__ = '0.0.9'
__version_date__ = '2017-10-08'


def checkCounts(infiles, outfiles):
    if len(infiles) == 0:
        print("INTERNAL ERROR: no infiles")
        sys.exit(1)
    if len(infiles) != len(outfiles):
        print("INTERNAL ERROR: " +
              "input count (%d) and output count (%d) differ" % (
                  len(infiles), len(outfiles)))
        sys.exit(1)
