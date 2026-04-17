# -*- coding: utf-8 -*-

"""
Character Vommitting. See https://goo.gl/MxONLX
"""

import re
import os

cjk_unified_part1 = '\u4E00', '\u62FF'
cjk_unified_part2 = '\u6300', '\u77FF'
cjk_unified_part3 = '\u7800', '\u8CFF'
cjk_unified_part4 = '\u8D00', '\u9FFF'

cjk_unified_ext_a = '\u3400', '\u4DBF'
cjk_unified_ext_b_part1 = '\U00020000', '\U000215FF'
cjk_unified_ext_b_part2 = '\U00021600', '\U000230FF'
cjk_unified_ext_b_part3 = '\U00023100', '\U000245FF'
cjk_unified_ext_b_part4 = '\U00024600', '\U000260FF'
cjk_unified_ext_b_part5 = '\U00026100', '\U000275FF'
cjk_unified_ext_b_part6 = '\U00027600', '\U000290FF'
cjk_unified_ext_b_part7 = '\U00029100', '\U0002A6DF'
cjk_unified_ext_c = '\U0002A700', '\U0002B73F'
cjk_unified_ext_d = '\U0002B740', '\U0002B81F'
cjk_unified_ext_e = '\U0002B820', '\U0002CEAF'

cjk_radicals_supplements = '\u2E80', '\u2EFF'
kangxi_radicals = '\u2F00', '\u2FDF'
ideographic_description_chars = '\u2FF0', '\u2FFF'
ideographic_desciption_chars = ideographic_description_chars  # back-compat alias (typo)
cjk_symbols_punctuations = '\u3000', '\u303F'
cjk_strokes = '\u31C0', '\u31EF'
enclosed_cjk_letters_months = '\u3200', '\u32FF'

cjk_compat = '\u3300', '\u33FF'
cjk_compat_ideographs = '\uF900', '\uFAFF'
cjk_compat_forms = '\uFE30', '\uFE4F'
enclosed_ideograph_supplement = '\U0001F200', '\U0001F2FF'
cjk_compat_ideographs_supplement = '\U0002F800', '\U0002FA1F'

hiragana =  '\u3040', '\u309F'
katakana =  '\u30A0', '\u30FF'
romanji =   '\uFF00', '\uFFEF' # Romanji with half-width katakan.

# Hangul syllables.
hangul_syllables =   '\uAC00', '\uD7AF'
hangul_syllables_assigned =   '\uAC00', '\uD7A3'
# Hangul Jamos.
hangul_jamo = '\u1100', '\u11FF'
hangul_jamo_modern_1 = '\u1100', '\u1112'
hangul_jamo_modern_2 = '\u1161', '\u1175'
hangul_jamo_modern_3 = '\u11A8', '\u11C2'
hangul_jamo_modern_all = [hangul_jamo_modern_1,
                          hangul_jamo_modern_2,
                          hangul_jamo_modern_3]
hangule_jamo_modern_all = hangul_jamo_modern_all  # back-compat alias (typo)
# HCJ
hangul_compat_jamo = '\u3130', '\u318F'
hangul_compat_jamo_assigned = '\u3131', '\u318E'
hangul_compat_jamo_assigned_all = [hangul_compat_jamo_assigned]
hangul_compat_jamo_modern_1 = '\u3131', '\u314E'
hangul_compat_jamo_modern_b = '\u314F', '\u3163'
hangul_compat_jamo_modern_all = [hangul_compat_jamo_modern_1,
                                 hangul_compat_jamo_modern_b]
hangul_compat_jamo_invalid = '\u3164'
# Hangul extensions
hangul_jamo_ext_a =  '\uA960', '\uA97F'
hangul_jamo_ext_a_assigned =  '\uA960', '\uA97C'
hangul_jamo_ext_b =  '\uD7B0', '\uD7FF'
hangul_jamo_ext_b_assigned_1 =  '\uD7B0', '\uD7C6'
hangul_jamo_ext_b_assigned_2 =  '\uD7CB', '\uD7FB'
# All assigned jamo
hangul_jamo_assigned_all = [hangul_jamo,
                            hangul_jamo_ext_a_assigned,
                            hangul_jamo_ext_b_assigned_1,
                            hangul_jamo_ext_b_assigned_2]

# From https://en.wikipedia.org/wiki/Bopomofo
bopomofo = '\u3100', '\u312F'
bopomofo_ext = '\u31A0', '\u31BF'

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
