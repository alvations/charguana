"""Smoke tests for charguana. Derived from README examples."""

from charguana import (
    get_charset,
    chinese_strokes,
    simplify,
    tradify,
    islang,
)
from charguana.viet import viet_ime, viet_tones


def test_hiragana_nonempty():
    chars = list(get_charset('hiragana'))
    assert 'あ' in chars
    assert 'ん' in chars


def test_katakana_nonempty():
    chars = list(get_charset('katakana'))
    assert 'ア' in chars
    assert 'ン' in chars


def test_bopomofo_nonempty():
    chars = list(get_charset('bopomofo'))
    assert 'ㄅ' in chars


def test_chinese_aliases_agree():
    zh = ''.join(get_charset('chinese'))
    assert zh == ''.join(get_charset('zh'))
    assert zh == ''.join(get_charset('cn'))


def test_japanese_aliases_agree():
    ja = ''.join(get_charset('japanese'))
    assert ja == ''.join(get_charset('ja'))
    assert ja == ''.join(get_charset('jp'))


def test_korean_aliases_agree():
    ko = ''.join(get_charset('korean'))
    assert ko == ''.join(get_charset('ko'))
    assert ko == ''.join(get_charset('kr'))


def test_thai_is_not_exhausted_across_calls():
    """Regression: get_charset('thai') used to return a pre-exhausted generator."""
    first = ''.join(get_charset('thai'))[:10]
    second = ''.join(get_charset('thai'))[:10]
    assert first == second == 'กขฃคฅฆงจฉช'


def test_simplify_tradify_roundtrip():
    assert simplify('錒') == '锕'
    assert tradify('锕') == '錒'


def test_chinese_strokes():
    assert chinese_strokes['绝'] == 9
    assert chinese_strokes['絕'] == 12


def test_perluniprops_currency():
    chars = ''.join(get_charset('Currency_Symbol'))
    assert '$' in chars
    assert '€' in chars
    assert '¥' in chars


def test_viet_tones():
    import unicodedata
    assert unicodedata.normalize('NFC', 'o' + viet_tones.sac) == 'ó'
    assert unicodedata.normalize('NFC', 'o' + viet_tones.huyen) == 'ò'
    assert unicodedata.normalize('NFC', 'o' + viet_tones.nang) == 'ọ'


def test_viet_ime_vni():
    assert viet_ime('Nguye64n Tra62n Anh Thu7') == 'Nguyễn Trần Anh Thư'


def test_viet_ime_telex():
    assert viet_ime('Nguyeefn Traafn Anh Thuw', mapping='telex') == 'Nguyền Trần Anh Thư'


def test_korean_is_hangul_char():
    """Regression: is_hangul_char referenced an undefined name."""
    from charguana.korean import is_hangul_char
    assert is_hangul_char('가') is True
    assert is_hangul_char('A') is False


def test_backcompat_typo_aliases():
    from charguana.cjk import (
        ideographic_description_chars,
        ideographic_desciption_chars,
        hangul_jamo_modern_all,
        hangule_jamo_modern_all,
    )
    assert ideographic_description_chars == ideographic_desciption_chars
    assert hangul_jamo_modern_all == hangule_jamo_modern_all


def test_unknown_charset_returns_empty():
    assert list(get_charset('not_a_real_charset')) == []


def test_viet_lower_u_is_not_empty_string():
    """Regression: lower_u_ngang was '' instead of 'u', so 'u' was missing from consonants."""
    from charguana.viet import lower_u_ngang, viet_consonants, u
    assert lower_u_ngang == 'u'
    assert 'u' in viet_consonants
    assert u[6:12] == ['u', 'ú', 'ù', 'ủ', 'ũ', 'ụ']


def test_vni_u7_tones():
    """Regression: VNI U7[1..5] used to route through o7, producing wrong vowel."""
    assert viet_ime('U73') == 'Ử'
    assert viet_ime('u75') == 'ự'
    assert viet_ime('Thu75') == 'Thự'


def test_vni_o_and_u_base_tones():
    """Regression: VNI O1..5 and U1..5 used to route through i[] (wrong vowel family)."""
    assert viet_ime('o1') == 'ó'
    assert viet_ime('u1') == 'ú'
    assert viet_ime('O2') == 'Ò'
    assert viet_ime('U4') == 'Ũ'


def test_telex_u_plus_and_o_plus():
    """Regression: telex Uws/Uwf/... mapped via o7, and Os/Us via i[]."""
    assert viet_ime('Uws', mapping='telex') == 'Ứ'
    assert viet_ime('Owf', mapping='telex') == 'Ờ'
    assert viet_ime('os', mapping='telex') == 'ó'
    assert viet_ime('us', mapping='telex') == 'ú'


def test_get_charset_returns_list():
    """0.2.0: get_charset returns a list, not a generator."""
    result = get_charset('hiragana')
    assert isinstance(result, list)
    # A list is reusable; a generator wouldn't be.
    assert len(result) == len(get_charset('hiragana'))


def test_iter_charset_is_lazy():
    """0.2.0: iter_charset returns an iterator."""
    from charguana import iter_charset
    it = iter_charset('hiragana')
    assert iter(it) is it  # iterators are their own iter


def test_islang_any_semantics():
    hira = get_charset('hiragana')
    assert islang('こんにちは', hira)
    assert islang('Aこ', hira)  # any-char match: mixed still matches
    assert not islang('hello', hira)  # no hiragana at all


def test_all_in_charset_requires_every_char():
    from charguana import all_in_charset
    hira = get_charset('hiragana')
    assert all_in_charset('こんにちは', hira)
    assert not all_in_charset('Aこ', hira)  # 'A' is not hiragana
    # vacuous truth
    assert all_in_charset('', hira)


def test_is_in_charsets_top_level():
    """0.2.0: is_in_charsets is re-exported at the top level."""
    from charguana import is_in_charsets
    from charguana.cjk import hangul_syllables_assigned
    assert is_in_charsets('가', [hangul_syllables_assigned])
    assert not is_in_charsets('A', [hangul_syllables_assigned])


def test_fetch_unichars_friendly_error(monkeypatch):
    """fetch_unichars should raise RuntimeError, not FileNotFoundError."""
    import subprocess
    from charguana.perluniprops import fetch_unichars

    def raise_fnf(*a, **kw):
        raise FileNotFoundError(2, 'No such file or directory', 'unichars')

    monkeypatch.setattr(subprocess, 'check_output', raise_fnf)
    try:
        fetch_unichars('Alpha')
    except RuntimeError as exc:
        assert 'unichars' in str(exc) and 'cpan' in str(exc)
    else:
        raise AssertionError('expected RuntimeError')


def test_importing_charguana_does_not_open_data_files():
    """Laziness: `import charguana` should not touch perluniprops or strokecounter files."""
    import builtins
    import importlib
    import sys

    # Drop any cached charguana modules so we get a fresh import.
    for mod in list(sys.modules):
        if mod == 'charguana' or mod.startswith('charguana.'):
            del sys.modules[mod]

    opened = []
    real_open = builtins.open

    def spy(*args, **kw):
        opened.append(str(args[0] if args else kw.get('file')))
        return real_open(*args, **kw)

    builtins.open = spy
    try:
        importlib.import_module('charguana')
    finally:
        builtins.open = real_open

    assert not any('perluniprops' in p for p in opened), opened
    assert not any('strokecounter' in p for p in opened), opened
