# xgo_py/xgoy/ant.py

from xgo import check_counts

__all__ = [  # CONSTANTS
    # FUNCTIONS
    'ant2xgo',
]


def ant2xgo_once(in_file, out_file,
                 dont_do_it=False, force=False, verbose=False):
    # SUPPRESS WARNINGS:
    _, _, _, _, _ = in_file, out_file, dont_do_it, force, verbose


def ant2xgo(in_files, out_files,
            dont_do_it=False, force=False, verbose=False):

    check_counts(in_files, out_files)

    for ndx, infile in enumerate(in_files):
        ant2xgo_once(infile, out_files[ndx], dont_do_it, force, verbose)
