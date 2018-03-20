# -*- coding: utf-8 -*-

from charguana.cjk import hangul_jamo_assigned_all, hangul_compat_jamo_assigned_all
from charguana.cjk import hangul_compat_jamo_modern_all, hangule_jamo_modern_all
from charguana.cjk import hangul_syllables_assigned

# Reference: http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646
# https://github.com/jonghwanhyeon/hangul-jamo/blob/master/hangul_jamo/constants.py

def is_in_charsets(character, charsets):
    """ Generic function to check if character between a list of charsets. """
    code = ord(character)
    return any(ord(start) <= code <= ord(end) for start, end in charsets)

def is_hcj(character):
    """
    Check if a single character is a Hangule Compatible Jamo (HCJ)
    HCJ is defined as the U+313x to U+318x block
    without two non-assigned code: U+318F and U+3164
    """
    return is_in_charsets(character, hangul_compat_jamo_assigned_all) and ord(character) != 0x3164

def is_jamo(character):
    """
    Check if a single character is a jamo character.
    Valid jamo includes all modern and archaic jamo, as well as all HCJ.
    Only check of assigned code points.
    """
    return is_in_charsets(character, hangul_jamo_assigned_all) or is_hcj(character)

def is_hcj_modern(character):
    """
    Check if a single character is a modern HCJ.
    See http://i18nl10n.com/korean/jamo.html
    """
    return is_in_charsets(character, hangul_compat_jamo_modern_all)

def is_jamo_modern(character):
    """
    Check if a single character is a modern jamo.
    See http://i18nl10n.com/korean/jamo.html
    """
    return is_in_charsets(character, hangule_jamo_modern_all) or is_hcj_modern(character)

def is_hangul_char(character):
    """
    Check if a single character is in the U+AC00 to U+D7A3 code block.
    """
    return is_in_charsets(characters, [hangul_syllables_assigned])
