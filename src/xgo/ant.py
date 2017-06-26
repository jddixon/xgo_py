# xgo_py/xgoy/ant.py

import sys

from xgo_py import checkCounts

__all__ = [  # CONSTANTS
    # FUNCTIONS
    'ant2xgo',
]


def ant2xgoOnce(inFile, outFile,
                dontDoIt=False, force=False, verbose=False):
    pass


def ant2xgo(inFiles, outFiles,
            dontDoIt=False, force=False, verbose=False):

    checkCounts(inFiles, outFiles)

    for index, inFile in enumerate(inFiles):

        ant2xgoOnce(infile, outFiles[ndx], dontDoIt, force, verbose)
