# xgo_py/xgoy/__init__.py

import sys

__all__ = [  # CONSTANTS
    '__version__', '__version_date__',
    # FUNCTIONS
    'checkCounts',
]

__version__ = '0.0.5'
__version_date__ = '2017-05-08'


def checkCounts(inFiles, outFiles):
    if len(inFiles) == 0:
        print("INTERNAL ERROR: no inFiles")
        sys.exit(1)
    if len(inFiles) != len(outFiles):
        print("INTERNAL ERROR: input count (%d) and output count (%d) differ" % (
            len(inFiles), len(outFiles)))
        sys.exit(1)
