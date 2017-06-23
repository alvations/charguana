# -*- coding: utf-8 -*-

"""
Thai Character Vommitting.
See https://en.wikipedia.org/wiki/Thai_(Unicode_block)
"""

thai_block = u'\u0e00', u'\u0e7f' # Unicode block, includes unassigned code points.

thai_consonants = u'\u0e01', u'\u0e2e'
thai_abbrev_mark = u'\u0e2f', u'\u0e2f' # pai-yan noi
thai_vowels_1 = u'\u0e30', u'\u0e3a'
thai_baht = u'\u0e3f', u'\u0e3f' # currency symbol.
thai_vowels_2 = u'\u0e40', u'\u0e46'
thai_diacritics = u'\u0e47', u'\u0e4e'
thai_others = u'\u0e4f', u'\u0e5b'

thai_utf8 = [thai_consonants, thai_abbrev_mark, thai_baht,
            thai_vowels_1, thai_vowels_2,
            thai_diacritics, thai_others]

# Shield the top level imports from all the local variables.
__all__ = ['thai_utf8', 'thai_block']
