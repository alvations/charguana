# -*- coding: utf-8 -*-

from charguana.cjk import *
from charguana.chinese import *
from charguana.chinese import chinese_strokes, simplify, tradify
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

from charguana import perluniprops as _perluniprops

# The file-backed props (IsAlpha, IsAlnum, IsLower, IsUpper, IsSo) are loaded
# on first access; resolving them through perluniprops.__getattr__ keeps
# `import charguana` cheap.
class _LazyCharsetMap:
    def __init__(self, static, lazy_names):
        self._static = static
        self._lazy_names = lazy_names

    def __contains__(self, key):
        return key in self._static or key in self._lazy_names

    def __getitem__(self, key):
        if key in self._static:
            return self._static[key]
        if key in self._lazy_names:
            return getattr(_perluniprops, self._lazy_names[key])
        raise KeyError(key)

    def keys(self):
        return list(self._static.keys()) + list(self._lazy_names.keys())

    def __iter__(self):
        return iter(self.keys())


perluniprops_charsets = _LazyCharsetMap(
    static={
        'Close_Punctuation': close_punctuation,
        'Open_Punctuation': open_punctuation,
        'Currency_Symbol': currency_symbol,
        'IsSc': is_sc,
        'IsN': is_n,
    },
    lazy_names={
        'IsAlnum': 'is_alnum',
        'IsAlpha': 'is_alpha',
        'IsLower': 'is_lower',
        'IsUpper': 'is_upper',
        'IsSo': 'is_so',
    },
)


def __getattr__(name):
    """Forward lazy perluniprops lookups so `from charguana import is_alpha` works."""
    lazy = {'is_alpha', 'is_alnum', 'is_lower', 'is_upper', 'is_so'}
    if name in lazy:
        return getattr(_perluniprops, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def get_chars_between(start, end):
    """Yield every character in the inclusive code point range [start, end]."""
    for i in range(ord(start), ord(end) + 1):
        yield chr(i)


def is_in_charsets(character, charsets):
    """Return True if ``character`` falls in any (start, end) tuple in ``charsets``."""
    code = ord(character)
    return any(ord(start) <= code <= ord(end) for start, end in charsets)


def get_cjk_charset(charset_name):
    """Yield every character in the named CJK charset (a lazy generator).

    Valid names: 'chinese' / 'zh' / 'cn', 'japanese' / 'ja' / 'jp',
    'korean' / 'ko' / 'kr', 'hiragana', 'katakana', 'hangul_syllables',
    'hangul_jamo', 'romanji', 'cjk_punctuation', 'bopomofo', 'cjk'.
    """
    for start, end in cjk_charsets[charset_name]:
        for char in get_chars_between(start, end):
            yield char


def get_charset_ranges(charset_ranges):
    """Yield every character spanned by an iterable of (start, end) code point tuples."""
    for start, end in charset_ranges:
        for char in get_chars_between(start, end):
            yield char


# Every value in ``other_charsets`` is a sequence of single characters
# (either an explicit list, a long string, or an expanded range). The Thai
# block is stored as (start, end) tuples in ``thai_utf8`` for reference; we
# expand it once here so the dict is shape-consistent with the others.
other_charsets = {
    'thai': list(get_charset_ranges(thai_utf8)),
    'viet': viet_utf8,
    'traditional_chinese': big5,
    'simplified_chinese': gbk,
}


def iter_charset(charset_name):
    """Return a lazy iterator over the characters in the named charset.

    Unlike :func:`get_charset`, this never materializes the full list. Useful
    for very large charsets (e.g. 'cjk') when you only need to scan them.

    Valid names: any key of ``cjk_charsets``, ``perluniprops_charsets``, or
    ``other_charsets`` — e.g. 'chinese', 'japanese', 'korean', 'thai', 'viet',
    'traditional_chinese', 'simplified_chinese', 'IsAlpha', 'IsN',
    'Open_Punctuation', 'Currency_Symbol', etc. Unknown names yield nothing.
    """
    if charset_name in cjk_charsets:
        return get_cjk_charset(charset_name)
    if charset_name in perluniprops_charsets:
        return iter(perluniprops_charsets[charset_name])
    if charset_name in other_charsets:
        return iter(other_charsets[charset_name])
    return iter(())


def get_charset(charset_name):
    """Return a ``list`` of characters in the named charset.

    Valid names: any key of ``cjk_charsets``, ``perluniprops_charsets``, or
    ``other_charsets`` — e.g. 'chinese', 'zh', 'japanese', 'ja', 'korean',
    'hiragana', 'katakana', 'bopomofo', 'thai', 'viet',
    'traditional_chinese', 'simplified_chinese', 'Open_Punctuation',
    'Close_Punctuation', 'Currency_Symbol', 'IsAlpha', 'IsAlnum', 'IsLower',
    'IsUpper', 'IsN', 'IsSo'. Unknown names return an empty list.

    Note: prior to 0.2.0 this returned a lazy iterator. Use
    :func:`iter_charset` if you need the old behavior.
    """
    return list(iter_charset(charset_name))


def islang(string, charset):
    """Return True if *any* character of ``string`` is in ``charset``.

    ``charset`` may be any iterable of characters (e.g. the output of
    :func:`get_charset`). See also :func:`all_in_charset` for a whole-string
    membership check.
    """
    charset_set = set(charset)
    return any(ch in charset_set for ch in string)


def all_in_charset(string, charset):
    """Return True if *every* character of ``string`` is in ``charset``.

    Empty ``string`` returns True (vacuous truth).
    """
    charset_set = set(charset)
    return all(ch in charset_set for ch in string)


__all__ = [
    # Chinese helpers
    'chinese_strokes', 'simplify', 'tradify',
    # CJK ranges / blocks
    'han_utf8', 'jap_utf8', 'kor_utf8',
    'hiragana', 'katakana', 'hangul_syllables', 'hangul_jamo',
    'bopomofo', 'cjk_symbols_punctuations', 'romanji',
    # Thai
    'thai_utf8', 'thai_block',
    # Vietnamese
    'viet_utf8', 'viet_tones', 'viet_consonants', 'viet_ime',
    # perluniprops
    'open_punctuation', 'close_punctuation', 'currency_symbol',
    'is_sc', 'is_alnum', 'is_alpha', 'is_lower', 'is_upper', 'is_n', 'is_so',
    # charset dispatch / utilities
    'cjk_charsets', 'perluniprops_charsets', 'other_charsets',
    'get_charset', 'iter_charset', 'get_cjk_charset', 'get_charset_ranges',
    'get_chars_between', 'is_in_charsets', 'islang', 'all_in_charset',
]
