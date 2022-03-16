#!/usr/bin/env nix-shell
#!nix-shell -p fontforge -i fontforge
import codecs
import glob
import os
import os.path

import fontforge

def all_files_of(root):
    for (dirpath, dirnames, filenames) in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def all_files():
    yield from all_files_of("content")
    yield from all_files_of("i18n")
    yield from all_files_of("layouts")
    yield from all_files_of("themes/m14n/layouts")

glyphs = set("Monday Tuesday Wednesday Thursday Friday Saturday Sunday Michcio's collection of picrews # | , Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec 0123456789")

for font_path in glob.glob("assets/*.ttf"):
    font = fontforge.open(font_path)
    for glyph in glyphs:
        font.selection[ord(glyph)] = True
    font.selection.invert()
    for glyph in font.selection.byGlyphs:
        font.removeGlyph(glyph)
    font.generate(font_path + '.trimmed.ttf')

