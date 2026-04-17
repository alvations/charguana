"""Emoji charset for charguana.

Bundles parsed Unicode emoji data under ``charguana/data/emoji/``. All
attributes are loaded lazily on first access — importing this module is free.

Public names::

    emoji_chars            frozenset[str]  — single-codepoint emoji
                                              (Emoji_Presentation property)
    emoji_sequences        list[str]       — keycap / flag / modifier sequences
    emoji_zwj_sequences    list[str]       — ZWJ compositions (🧑‍💻 etc.)
    emoji_properties       dict[str, frozenset[str]]
                                           — char → UCD emoji-data properties

Functions::

    is_emoji(s)            — True if s is a single emoji char or a known
                             multi-char emoji sequence
    fetch_emoji(version)   — download + parse fresh data from unicode.org
                             (no side effects on disk)
"""

from __future__ import annotations

import os
import urllib.request

emoji_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'emoji')

# UCD and the emoji spec expose data at two different URL roots.
_UCD_LATEST_URL = "https://unicode.org/Public/UCD/latest/ucd/emoji/{name}"
_UCD_VERSIONED_URL = "https://unicode.org/Public/{ver}.0/ucd/emoji/{name}"
_EMOJI_URL = "https://unicode.org/Public/emoji/{ver}/{name}"

_SOURCES = {
    "emoji-data.txt": "ucd",
    "emoji-variation-sequences.txt": "ucd",
    "emoji-sequences.txt": "emoji",
    "emoji-zwj-sequences.txt": "emoji",
}


# ---------------------------------------------------------------------------
# Lazy bundled data
# ---------------------------------------------------------------------------

_cache: dict[str, object] = {}


def _load_chars() -> frozenset[str]:
    with open(os.path.join(emoji_dir, 'emoji_chars.txt'), encoding='utf-8') as fin:
        return frozenset(line for line in fin.read().splitlines() if line)


def _load_sequences(filename: str) -> list[str]:
    with open(os.path.join(emoji_dir, filename), encoding='utf-8') as fin:
        return [line for line in fin.read().splitlines() if line]


def _load_properties() -> dict[str, frozenset[str]]:
    path = os.path.join(emoji_dir, 'emoji_properties.txt')
    result: dict[str, frozenset[str]] = {}
    with open(path, encoding='utf-8') as fin:
        for line in fin:
            line = line.rstrip('\n')
            if not line or '\t' not in line:
                continue
            ch, props = line.split('\t', 1)
            result[ch] = frozenset(props.split(','))
    return result


_LOADERS = {
    'emoji_chars': _load_chars,
    'emoji_sequences': lambda: _load_sequences('emoji_sequences.txt'),
    'emoji_zwj_sequences': lambda: _load_sequences('emoji_zwj_sequences.txt'),
    'emoji_properties': _load_properties,
}


def __getattr__(name):
    """PEP 562 lazy loader for bundled emoji data."""
    if name in _LOADERS:
        if name not in _cache:
            _cache[name] = _LOADERS[name]()
        return _cache[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def is_emoji(s: str) -> bool:
    """Return True if ``s`` is a known emoji character or sequence.

    Matches single-codepoint emoji (Emoji_Presentation) and any named
    sequence — keycaps, flags, skin-tone modifier sequences, and ZWJ
    compositions. Text-style variation selectors are not included.
    """
    if not s:
        return False
    chars = __getattr__('emoji_chars')  # trigger lazy load
    if len(s) == 1 and s in chars:
        return True
    seqs = __getattr__('emoji_sequences')
    zwj = __getattr__('emoji_zwj_sequences')
    return s in seqs or s in zwj


# ---------------------------------------------------------------------------
# Runtime fetch (escape hatch for users who want fresh data)
# ---------------------------------------------------------------------------

def _iter_data_lines(text: str):
    for line in text.splitlines():
        line = line.split('#', 1)[0].strip()
        if line:
            yield line


def _expand_codepoints(field: str) -> list[str]:
    field = field.strip()
    if '..' in field:
        start_hex, end_hex = field.split('..')
        return [chr(c) for c in range(int(start_hex, 16), int(end_hex, 16) + 1)]
    parts = field.split()
    return [''.join(chr(int(p, 16)) for p in parts)]


def _parse_emoji_data(text: str) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for line in _iter_data_lines(text):
        cps_field, prop = (s.strip() for s in line.split(';', 1))
        for ch in _expand_codepoints(cps_field):
            result.setdefault(prop, set()).add(ch)
    return result


def _parse_sequences(text: str) -> list[str]:
    out: list[str] = []
    for line in _iter_data_lines(text):
        out.extend(_expand_codepoints(line.split(';', 1)[0]))
    return out


def _parse_variation_sequences(text: str) -> list[str]:
    out: list[str] = []
    for line in _iter_data_lines(text):
        fields = [s.strip() for s in line.split(';')]
        if len(fields) >= 2 and 'emoji' in fields[1]:
            out.extend(_expand_codepoints(fields[0]))
    return out


def _fetch_source(name: str, version: str) -> str:
    source = _SOURCES[name]
    if source == 'ucd':
        url = (
            _UCD_LATEST_URL.format(name=name)
            if version == 'latest'
            else _UCD_VERSIONED_URL.format(ver=version, name=name)
        )
    else:
        url = _EMOJI_URL.format(ver=version, name=name)
    with urllib.request.urlopen(url, timeout=30) as resp:
        return resp.read().decode('utf-8')


def fetch_emoji(version: str = 'latest') -> dict[str, object]:
    """Download and parse fresh emoji data from unicode.org.

    Returns a dict with keys ``data_properties`` (``dict[str, set[str]]``),
    ``sequences`` (``list[str]``), ``zwj_sequences`` (``list[str]``), and
    ``variation_sequences`` (``list[str]``). This function hits the network
    and does not touch the on-disk bundled data.

    ``version`` may be ``'latest'`` (default), or a pinned major.minor like
    ``'16.0'``. Requires connectivity to unicode.org.
    """
    return {
        'data_properties': _parse_emoji_data(_fetch_source('emoji-data.txt', version)),
        'sequences': _parse_sequences(_fetch_source('emoji-sequences.txt', version)),
        'zwj_sequences': _parse_sequences(_fetch_source('emoji-zwj-sequences.txt', version)),
        'variation_sequences': _parse_variation_sequences(
            _fetch_source('emoji-variation-sequences.txt', version)
        ),
    }


# `__all__` excludes the lazy data names on purpose — listing them would make
# `from charguana.emoji import *` resolve every one and defeat lazy loading.
# They remain accessible via explicit attribute access (`charguana.emoji.emoji_chars`)
# or explicit import (`from charguana.emoji import emoji_chars`).
__all__ = ['is_emoji', 'fetch_emoji']
