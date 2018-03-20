# -*- coding: utf-8 -*-

"""
Character Vommitting. See https://goo.gl/MxONLX
"""

import re
import os

cjk_unified_part1 = u'\u4E00', u'\u62FF'
cjk_unified_part2 = u'\u6300', u'\u77FF'
cjk_unified_part3 = u'\u7800', u'\u8CFF'
cjk_unified_part4 = u'\u8D00', u'\u9FFF'

cjk_unified_ext_a = u'\u3400', u'\u4DBF'
cjk_unified_ext_b_part1 = u'\U00020000', u'\U000215FF'
cjk_unified_ext_b_part2 = u'\U00021600', u'\U000230FF'
cjk_unified_ext_b_part3 = u'\U00023100', u'\U000245FF'
cjk_unified_ext_b_part4 = u'\U00024600', u'\U000260FF'
cjk_unified_ext_b_part5 = u'\U00026100', u'\U000275FF'
cjk_unified_ext_b_part6 = u'\U00027600', u'\U000290FF'
cjk_unified_ext_b_part7 = u'\U00029100', u'\U0002A6DF'
cjk_unified_ext_c = u'\U0002A700', u'\U0002B73F'
cjk_unified_ext_d = u'\U0002B740', u'\U0002B81F'
cjk_unified_ext_e = u'\U0002B820', u'\U0002CEAF'

cjk_radicals_supplements = u'\u2E80', u'\u2EFF'
kangxi_radicals = u'\u2F00', u'\u2FDF'
ideographic_desciption_chars = u'\u2FF0', u'\u2FFF'
cjk_symbols_punctuations = u'\u3000', u'\u303F'
cjk_strokes = u'\u31C0', u'\u31EF'
enclosed_cjk_letters_months = u'\u3200', u'\u32FF'

cjk_compat = u'\u3300', u'\u33FF'
cjk_compat_ideographs = u'\uF900', u'\uFAFF'
cjk_compat_forms = u'\uFE30', u'\uFE4F'
enclosed_ideograph_supplement = u'\U0001F200', u'\U0001F2FF'
cjk_compat_ideographs_supplement = u'\U0002F800', u'\U0002FA1F'

hiragana =  u'\u3040', u'\u309F'
katakana =  u'\u30A0', u'\u30FF'
romanji =   u'\uFF00', u'\uFFEF' # Romanji with half-width katakan.

hangul_syllables =   u'\uAC00', u'\uD7AF'
hangul_jamo =        u'\u1100', u'\u11FF'
hangul_compat_jamo = u'\u3130', u'\u318F'
hangul_jamo_ext_a =  u'\uA960', u'\uA97F'
hangul_jamo_ext_b =  u'\uD7B0', u'\uD7FF'

# From https://en.wikipedia.org/wiki/Bopomofo
bopomofo = u'\u3100', u'\u312F'
bopomofo_ext = u'\u31A0', u'\u31BF'

# All UTF-8 Chinese character sets.
# From https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_(Unicode_block)
han_utf8 = [cjk_unified_part1, cjk_unified_part2, cjk_unified_part3,
            cjk_unified_part4, cjk_unified_ext_a,
            cjk_radicals_supplements, kangxi_radicals,
            ideographic_desciption_chars, cjk_symbols_punctuations,
            cjk_strokes, enclosed_cjk_letters_months, cjk_compat,
            cjk_compat_ideographs, cjk_compat_forms]

# All UTF-16 Chinese character sets.
# From https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_(Unicode_block)
han_utf16 = [cjk_unified_ext_b_part1,
            cjk_unified_ext_b_part2, cjk_unified_ext_b_part3,
            cjk_unified_ext_b_part4, cjk_unified_ext_b_part5,
            cjk_unified_ext_b_part6, cjk_unified_ext_b_part7,
            cjk_unified_ext_c, cjk_unified_ext_d, cjk_unified_ext_e,
            enclosed_ideograph_supplement, cjk_compat_ideographs_supplement]

# All UTF-8 Japanese character sets.
# From http://www.rikai.com/library/kanjitables/kanji_codes.unicode.shtml
jap_utf8 = [hiragana, katakana,
            cjk_unified_part1, cjk_unified_part2,  # Common + Uncommon Kanji.
            cjk_unified_part3, cjk_unified_part4,  # Common + Uncommon Kanji.
            cjk_unified_ext_a,  # Rare Kanji.
            cjk_symbols_punctuations
            ]


# All UTF-8 Korean character sets.
# From https://en.wikipedia.org/wiki/Hangul
kor_utf8 = [hangul_syllables, hangul_jamo, hangul_compat_jamo,
            hangul_jamo_ext_a, hangul_jamo_ext_b,
            cjk_symbols_punctuations]


# Shield the top level imports from all the local variables.
__all__ = ['han_utf8', 'jap_utf8', 'kor_utf8',
           'hiragana', 'katakana', 'hangul_syllables', 'hangul_jamo',
           'bopomofo', 'cjk_symbols_punctuations', 'romanji']
