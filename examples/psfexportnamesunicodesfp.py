#!/usr/bin/env python3
'''Outputs an unsorted csv file containing the names of all the glyphs in the default layer
and their primary unicode values. Format name,usv'''
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2018 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

from silfont.core import execute
from fontParts.world import *

suffix = "_namesunicodes"

# Setting input - For fontParts you specify filename for input
argspec = [
    ('ifont', {'help': 'Input font file'}, {'type': 'filename'}),
    ('-o','--output',{'help': 'Output csv file'}, {'type': 'outfile', 'def': suffix+'.csv'})]

def doit(args) :
    font = OpenFont(args.ifont)
    outfile = args.output

    for glyph in font:
        unival = ""
        if glyph.unicode:
            unival = str.upper(hex(glyph.unicode))[2:7].zfill(4)
        outfile.write(glyph.name + "," + unival + "\n")

    print("Done")

# Note the use of None rather than "UFO" in this execute()
def cmd() : execute(None,doit,argspec)
if __name__ == "__main__": cmd()
