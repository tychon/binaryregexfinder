#!/usr/bin/python3

# Finds byte-occurrences in binary files and saves the following data to
# separate files.
#
# Usage:
#     regexfind.py PATTERNFILE INPUT LENGTH OUTDIR
#
# PATTERNFILE a file containing the regular expression
# INPUT the input file
# LENGTH number of bytes after begin of pattern to extract
# OUTDIR directory where extracted data goes

import sys
import re
import mmap

if len(sys.argv) != 5:
    print("Give 5 arguments.")
    sys.exit(1)

with open(sys.argv[1], 'br') as f:
    regbase = f.read()

regex = re.compile(regbase)
length = int(sys.argv[3])

outdir = sys.argv[4]
counter = 1

with open(sys.argv[2], 'br') as fin:
    m = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)
    for mo in regex.finditer(m):
        print("%5d. occurrence at byte %15d"%(counter, mo.start()))
        fname = outdir+'/found%05d'%counter
        with open(fname, 'bw+') as fout:
            fout.write(m[mo.start():mo.start()+length])
        counter += 1
