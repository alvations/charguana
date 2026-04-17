# -*- coding: utf-8 -*-

import os
import subprocess

perluniprops_dir = os.path.dirname(os.path.abspath(__file__)) + '/data/perluniprops/'


def fetch_unichars(charset_name):
    r"""Call the external ``unichars`` command and return the matched characters.

    ``unichars`` is a Perl tool from Unicode::Tussle. Install with::

        cpan Unicode::Tussle

    Returns the concatenation of every character matching
    ``\p{charset_name}``. Raises :class:`RuntimeError` with an install hint if
    ``unichars`` is not on ``$PATH``.
    """
    try:
        out = subprocess.check_output(['unichars', r'\p{' + charset_name + '}'])
    except FileNotFoundError as exc:
        raise RuntimeError(
            "The `unichars` command is not on $PATH. "
            "Install it with `cpan Unicode::Tussle` (Perl's CPAN)."
        ) from exc
    # `unichars` output: one record per line, the character is the 2nd
    # whitespace-separated field.
    return ''.join(line.split()[1] for line in out.decode('utf-8').splitlines() if line.split())


close_punctuation = [')', ']', '}', '\u0f3b', '\u0f3d', '\u169c',
    '\u2046', '\u207e', '\u208e', '\u232a', '\u2769', '\u276b', '\u276d',
    '\u276f', '\u2771', '\u2773', '\u2775', '\u27c6', '\u27e7', '\u27e9',
    '\u27eb', '\u27ed', '\u27ef', '\u2984', '\u2986', '\u2988', '\u298a',
    '\u298c', '\u298e', '\u2990', '\u2992', '\u2994', '\u2996', '\u2998',
    '\u29d9', '\u29db', '\u29fd', '\u2e23', '\u2e25', '\u2e27', '\u2e29',
    '\u3009', '\u300b', '\u300d', '\u300f', '\u3011', '\u3015', '\u3017',
    '\u3019', '\u301b', '\u301e', '\u301f', '\ufd3f', '\ufe18', '\ufe36',
    '\ufe38', '\ufe3a', '\ufe3c', '\ufe3e', '\ufe40', '\ufe42', '\ufe44',
    '\ufe48', '\ufe5a', '\ufe5c', '\ufe5e', '\uff09', '\uff3d', '\uff5d',
    '\uff60', '\uff63']

open_punctuation = ['(', '[', '{', '\u0f3a', '\u0f3c', '\u169b',
    '\u201a', '\u201e', '\u2045', '\u207d', '\u208d', '\u2329', '\u2768',
    '\u276a', '\u276c', '\u276e', '\u2770', '\u2772', '\u2774', '\u27c5',
    '\u27e6', '\u27e8', '\u27ea', '\u27ec', '\u27ee', '\u2983', '\u2985',
    '\u2987', '\u2989', '\u298b', '\u298d', '\u298f', '\u2991', '\u2993',
    '\u2995', '\u2997', '\u29d8', '\u29da', '\u29fc', '\u2e22', '\u2e24',
    '\u2e26', '\u2e28', '\u3008', '\u300a', '\u300c', '\u300e', '\u3010',
    '\u3014', '\u3016', '\u3018', '\u301a', '\u301d', '\ufd3e', '\ufe17',
    '\ufe35', '\ufe37', '\ufe39', '\ufe3b', '\ufe3d', '\ufe3f', '\ufe41',
    '\ufe43', '\ufe47', '\ufe59', '\ufe5b', '\ufe5d', '\uff08', '\uff3b',
    '\uff5b', '\uff5f', '\uff62']

is_sc = currency_symbol = ['$', '\xa2', '\xa3', '\xa4', '\xa5', '\u058f',
    '\u060b', '\u09f2', '\u09f3', '\u09fb', '\u0af1', '\u0bf9', '\u0e3f',
    '\u17db', '\u20a0', '\u20a1', '\u20a2', '\u20a3', '\u20a4', '\u20a5',
    '\u20a6', '\u20a7', '\u20a8', '\u20a9', '\u20aa', '\u20ab', '\u20ac',
    '\u20ad', '\u20ae', '\u20af', '\u20b0', '\u20b1', '\u20b2', '\u20b3',
    '\u20b4', '\u20b5', '\u20b6', '\u20b7', '\u20b8', '\u20b9', '\u20ba',
    '\ua838', '\ufdfc', '\ufe69', '\uff04', '\uffe0', '\uffe1', '\uffe5',
    '\uffe6']

# File-backed properties are loaded lazily on first attribute access.
# This avoids reading ~200 KB of data at import time for users who only need
# the CJK / Thai / Viet charsets.
_file_backed = {
    'is_so':    'IsSo.txt',
    'is_alpha': 'IsAlpha.txt',
    'is_alnum': 'IsAlnum.txt',
    'is_lower': 'IsLower.txt',
    'is_upper': 'IsUpper.txt',
}
_cache = {}


def __getattr__(name):
    """PEP 562 module-level lazy loader for file-backed uniprops."""
    if name in _file_backed:
        if name not in _cache:
            path = os.path.join(perluniprops_dir, _file_backed[name])
            with open(path, encoding='utf-8') as fin:
                _cache[name] = list(fin.read())
        return _cache[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

is_n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\xb2',
    '\xb3', '\xb9', '\xbc', '\xbd', '\xbe', '\u0660', '\u0661', '\u0662',
    '\u0663', '\u0664', '\u0665', '\u0666', '\u0667', '\u0668', '\u0669',
    '\u06f0', '\u06f1', '\u06f2', '\u06f3', '\u06f4', '\u06f5', '\u06f6',
    '\u06f7', '\u06f8', '\u06f9', '\u07c0', '\u07c1', '\u07c2', '\u07c3',
    '\u07c4', '\u07c5', '\u07c6', '\u07c7', '\u07c8', '\u07c9', '\u0966',
    '\u0967', '\u0968', '\u0969', '\u096a', '\u096b', '\u096c', '\u096d',
    '\u096e', '\u096f', '\u09e6', '\u09e7', '\u09e8', '\u09e9', '\u09ea',
    '\u09eb', '\u09ec', '\u09ed', '\u09ee', '\u09ef', '\u09f4', '\u09f5',
    '\u09f6', '\u09f7', '\u09f8', '\u09f9', '\u0a66', '\u0a67', '\u0a68',
    '\u0a69', '\u0a6a', '\u0a6b', '\u0a6c', '\u0a6d', '\u0a6e', '\u0a6f',
    '\u0ae6', '\u0ae7', '\u0ae8', '\u0ae9', '\u0aea', '\u0aeb', '\u0aec',
    '\u0aed', '\u0aee', '\u0aef', '\u0b66', '\u0b67', '\u0b68', '\u0b69',
    '\u0b6a', '\u0b6b', '\u0b6c', '\u0b6d', '\u0b6e', '\u0b6f', '\u0b72',
    '\u0b73', '\u0b74', '\u0b75', '\u0b76', '\u0b77', '\u0be6', '\u0be7',
    '\u0be8', '\u0be9', '\u0bea', '\u0beb', '\u0bec', '\u0bed', '\u0bee',
    '\u0bef', '\u0bf0', '\u0bf1', '\u0bf2', '\u0c66', '\u0c67', '\u0c68',
    '\u0c69', '\u0c6a', '\u0c6b', '\u0c6c', '\u0c6d', '\u0c6e', '\u0c6f',
    '\u0c78', '\u0c79', '\u0c7a', '\u0c7b', '\u0c7c', '\u0c7d', '\u0c7e',
    '\u0ce6', '\u0ce7', '\u0ce8', '\u0ce9', '\u0cea', '\u0ceb', '\u0cec',
    '\u0ced', '\u0cee', '\u0cef', '\u0d66', '\u0d67', '\u0d68', '\u0d69',
    '\u0d6a', '\u0d6b', '\u0d6c', '\u0d6d', '\u0d6e', '\u0d6f', '\u0d70',
    '\u0d71', '\u0d72', '\u0d73', '\u0d74', '\u0d75', '\u0e50', '\u0e51',
    '\u0e52', '\u0e53', '\u0e54', '\u0e55', '\u0e56', '\u0e57', '\u0e58',
    '\u0e59', '\u0ed0', '\u0ed1', '\u0ed2', '\u0ed3', '\u0ed4', '\u0ed5',
    '\u0ed6', '\u0ed7', '\u0ed8', '\u0ed9', '\u0f20', '\u0f21', '\u0f22',
    '\u0f23', '\u0f24', '\u0f25', '\u0f26', '\u0f27', '\u0f28', '\u0f29',
    '\u0f2a', '\u0f2b', '\u0f2c', '\u0f2d', '\u0f2e', '\u0f2f', '\u0f30',
    '\u0f31', '\u0f32', '\u0f33', '\u1040', '\u1041', '\u1042', '\u1043',
    '\u1044', '\u1045', '\u1046', '\u1047', '\u1048', '\u1049', '\u1090',
    '\u1091', '\u1092', '\u1093', '\u1094', '\u1095', '\u1096', '\u1097',
    '\u1098', '\u1099', '\u1369', '\u136a', '\u136b', '\u136c', '\u136d',
    '\u136e', '\u136f', '\u1370', '\u1371', '\u1372', '\u1373', '\u1374',
    '\u1375', '\u1376', '\u1377', '\u1378', '\u1379', '\u137a', '\u137b',
    '\u137c', '\u16ee', '\u16ef', '\u16f0', '\u17e0', '\u17e1', '\u17e2',
    '\u17e3', '\u17e4', '\u17e5', '\u17e6', '\u17e7', '\u17e8', '\u17e9',
    '\u17f0', '\u17f1', '\u17f2', '\u17f3', '\u17f4', '\u17f5', '\u17f6',
    '\u17f7', '\u17f8', '\u17f9', '\u1810', '\u1811', '\u1812', '\u1813',
    '\u1814', '\u1815', '\u1816', '\u1817', '\u1818', '\u1819', '\u1946',
    '\u1947', '\u1948', '\u1949', '\u194a', '\u194b', '\u194c', '\u194d',
    '\u194e', '\u194f', '\u19d0', '\u19d1', '\u19d2', '\u19d3', '\u19d4',
    '\u19d5', '\u19d6', '\u19d7', '\u19d8', '\u19d9', '\u19da', '\u1a80',
    '\u1a81', '\u1a82', '\u1a83', '\u1a84', '\u1a85', '\u1a86', '\u1a87',
    '\u1a88', '\u1a89', '\u1a90', '\u1a91', '\u1a92', '\u1a93', '\u1a94',
    '\u1a95', '\u1a96', '\u1a97', '\u1a98', '\u1a99', '\u1b50', '\u1b51',
    '\u1b52', '\u1b53', '\u1b54', '\u1b55', '\u1b56', '\u1b57', '\u1b58',
    '\u1b59', '\u1bb0', '\u1bb1', '\u1bb2', '\u1bb3', '\u1bb4', '\u1bb5',
    '\u1bb6', '\u1bb7', '\u1bb8', '\u1bb9', '\u1c40', '\u1c41', '\u1c42',
    '\u1c43', '\u1c44', '\u1c45', '\u1c46', '\u1c47', '\u1c48', '\u1c49',
    '\u1c50', '\u1c51', '\u1c52', '\u1c53', '\u1c54', '\u1c55', '\u1c56',
    '\u1c57', '\u1c58', '\u1c59', '\u2070', '\u2074', '\u2075', '\u2076',
    '\u2077', '\u2078', '\u2079', '\u2080', '\u2081', '\u2082', '\u2083',
    '\u2084', '\u2085', '\u2086', '\u2087', '\u2088', '\u2089', '\u2150',
    '\u2151', '\u2152', '\u2153', '\u2154', '\u2155', '\u2156', '\u2157',
    '\u2158', '\u2159', '\u215a', '\u215b', '\u215c', '\u215d', '\u215e',
    '\u215f', '\u2160', '\u2161', '\u2162', '\u2163', '\u2164', '\u2165',
    '\u2166', '\u2167', '\u2168', '\u2169', '\u216a', '\u216b', '\u216c',
    '\u216d', '\u216e', '\u216f', '\u2170', '\u2171', '\u2172', '\u2173',
    '\u2174', '\u2175', '\u2176', '\u2177', '\u2178', '\u2179', '\u217a',
    '\u217b', '\u217c', '\u217d', '\u217e', '\u217f', '\u2180', '\u2181',
    '\u2182', '\u2185', '\u2186', '\u2187', '\u2188', '\u2189', '\u2460',
    '\u2461', '\u2462', '\u2463', '\u2464', '\u2465', '\u2466', '\u2467',
    '\u2468', '\u2469', '\u246a', '\u246b', '\u246c', '\u246d', '\u246e',
    '\u246f', '\u2470', '\u2471', '\u2472', '\u2473', '\u2474', '\u2475',
    '\u2476', '\u2477', '\u2478', '\u2479', '\u247a', '\u247b', '\u247c',
    '\u247d', '\u247e', '\u247f', '\u2480', '\u2481', '\u2482', '\u2483',
    '\u2484', '\u2485', '\u2486', '\u2487', '\u2488', '\u2489', '\u248a',
    '\u248b', '\u248c', '\u248d', '\u248e', '\u248f', '\u2490', '\u2491',
    '\u2492', '\u2493', '\u2494', '\u2495', '\u2496', '\u2497', '\u2498',
    '\u2499', '\u249a', '\u249b', '\u24ea', '\u24eb', '\u24ec', '\u24ed',
    '\u24ee', '\u24ef', '\u24f0', '\u24f1', '\u24f2', '\u24f3', '\u24f4',
    '\u24f5', '\u24f6', '\u24f7', '\u24f8', '\u24f9', '\u24fa', '\u24fb',
    '\u24fc', '\u24fd', '\u24fe', '\u24ff', '\u2776', '\u2777', '\u2778',
    '\u2779', '\u277a', '\u277b', '\u277c', '\u277d', '\u277e', '\u277f',
    '\u2780', '\u2781', '\u2782', '\u2783', '\u2784', '\u2785', '\u2786',
    '\u2787', '\u2788', '\u2789', '\u278a', '\u278b', '\u278c', '\u278d',
    '\u278e', '\u278f', '\u2790', '\u2791', '\u2792', '\u2793', '\u2cfd',
    '\u3192', '\u3193', '\u3194', '\u3195', '\u3220', '\u3221', '\u3222',
    '\u3223', '\u3224', '\u3225', '\u3226', '\u3227', '\u3228', '\u3229',
    '\u3248', '\u3249', '\u324a', '\u324b', '\u324c', '\u324d', '\u324e',
    '\u324f', '\u3251', '\u3252', '\u3253', '\u3254', '\u3255', '\u3256',
    '\u3257', '\u3258', '\u3259', '\u325a', '\u325b', '\u325c', '\u325d',
    '\u325e', '\u325f', '\u3280', '\u3281', '\u3282', '\u3283', '\u3284',
    '\u3285', '\u3286', '\u3287', '\u3288', '\u3289', '\u32b1', '\u32b2',
    '\u32b3', '\u32b4', '\u32b5', '\u32b6', '\u32b7', '\u32b8', '\u32b9',
    '\u32ba', '\u32bb', '\u32bc', '\u32bd', '\u32be', '\u32bf', '\ua620',
    '\ua621', '\ua622', '\ua623', '\ua624', '\ua625', '\ua626', '\ua627',
    '\ua628', '\ua629', '\ua6e6', '\ua6e7', '\ua6e8', '\ua6e9', '\ua6ea',
    '\ua6eb', '\ua6ec', '\ua6ed', '\ua6ee', '\ua6ef', '\ua830', '\ua831',
    '\ua832', '\ua833', '\ua834', '\ua835', '\ua8d0', '\ua8d1', '\ua8d2',
    '\ua8d3', '\ua8d4', '\ua8d5', '\ua8d6', '\ua8d7', '\ua8d8', '\ua8d9',
    '\ua900', '\ua901', '\ua902', '\ua903', '\ua904', '\ua905', '\ua906',
    '\ua907', '\ua908', '\ua909', '\ua9d0', '\ua9d1', '\ua9d2', '\ua9d3',
    '\ua9d4', '\ua9d5', '\ua9d6', '\ua9d7', '\ua9d8', '\ua9d9', '\uaa50',
    '\uaa51', '\uaa52', '\uaa53', '\uaa54', '\uaa55', '\uaa56', '\uaa57',
    '\uaa58', '\uaa59', '\uabf0', '\uabf1', '\uabf2', '\uabf3', '\uabf4',
    '\uabf5', '\uabf6', '\uabf7', '\uabf8', '\uabf9', '\uff10', '\uff11',
    '\uff12', '\uff13', '\uff14', '\uff15', '\uff16', '\uff17', '\uff18',
    '\uff19']

# `__all__` intentionally excludes the file-backed names (is_alpha, is_alnum,
# is_lower, is_upper, is_so). Listing them would cause `from perluniprops
# import *` to eagerly resolve every lazy name, defeating lazy loading.
# They are still accessible via explicit attribute access or explicit import.
__all__ = ['close_punctuation', 'open_punctuation', 'currency_symbol',
           'is_sc', 'is_n', 'fetch_unichars']
