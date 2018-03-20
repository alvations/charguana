# -*- coding: utf-8 -*-

from charguana.cjk import *
from charguana.chinese import *
from charguana.perluniprops import *
from charguana.thai import *
from charguana.viet import *

cjk_charsets = {'chinese': han_utf8, 'zh': han_utf8, 'cn': han_utf8,
                'japanese': jap_utf8, 'ja': jap_utf8, 'jp': jap_utf8,
                'hiragana': [hiragana], 'katakana': [katakana],
                'korean': kor_utf8, 'ko':kor_utf8, 'kr':kor_utf8,
                'hangul_syllables': [hangul_syllables], 'hangul_jamo': [hangul_jamo],
                'romanji': [romanji], 'cjk_punctuation': [cjk_symbols_punctuations],
                'bopomofo': [bopomofo],
                'cjk': sorted(set(han_utf8 + jap_utf8 + kor_utf8 + [romanji])),
                }

perluniprops_charsets = {'Close_Punctuation': close_punctuation,
                         'Open_Punctuation': open_punctuation,
                         'Currency_Symbol': currency_symbol, 'IsSc': is_sc,
                         'IsAlnum': is_alnum, 'IsAlpha': is_alpha,
                         'IsLower': is_lower, 'IsUpper': is_upper,
                         'IsN': is_n, 'IsSo': is_so}

def get_chars_between(start, end):
    for i in range(ord(start), ord(end)+1):
        yield chr(i)

def get_cjk_charset(charset_name):
    for start, end in cjk_charsets[charset_name]:
        for char in get_chars_between(start, end):
            yield char

def get_charset_ranges(charset_ranges):
    for start, end in charset_ranges:
        for char in get_chars_between(start, end):
            yield char

def islang(string, charset):
    return any(set(string).intersection(charset))

other_charsets = {'thai': get_charset_ranges(thai_utf8), 'viet': viet_utf8,
                  'traditional_chinese': big5, 'simplified_chinese': gbk}

def get_charset(charset_name):
    if charset_name in cjk_charsets:
        return get_cjk_charset(charset_name)
    elif charset_name in perluniprops_charsets:
        return iter(perluniprops_charsets[charset_name])
    elif charset_name in other_charsets:
        return iter(other_charsets[charset_name])
    else:
        return iter([])
