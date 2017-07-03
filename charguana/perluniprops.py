# -*- coding: utf-8 -*-

import io
import os
import subprocess

perluniprops_dir = os.path.dirname(os.path.abspath(__file__)) + '/data/perluniprops/'

def fetch_unichars(charset_name):
    """
    It's necessary to install the `unichars` command first using:
        $ cpan Unicode::Tussle
    """
    cmd = "unichars '\p{" + charset_name + "}' | cut -f2 -d' ' | tr -d '\n'"
    return subprocess.check_output(cmd, shell=True).decode('utf8')


close_punctuation = [u')', u']', u'}', u'\u0f3b', u'\u0f3d', u'\u169c',
    u'\u2046', u'\u207e', u'\u208e', u'\u232a', u'\u2769', u'\u276b', u'\u276d',
    u'\u276f', u'\u2771', u'\u2773', u'\u2775', u'\u27c6', u'\u27e7', u'\u27e9',
    u'\u27eb', u'\u27ed', u'\u27ef', u'\u2984', u'\u2986', u'\u2988', u'\u298a',
    u'\u298c', u'\u298e', u'\u2990', u'\u2992', u'\u2994', u'\u2996', u'\u2998',
    u'\u29d9', u'\u29db', u'\u29fd', u'\u2e23', u'\u2e25', u'\u2e27', u'\u2e29',
    u'\u3009', u'\u300b', u'\u300d', u'\u300f', u'\u3011', u'\u3015', u'\u3017',
    u'\u3019', u'\u301b', u'\u301e', u'\u301f', u'\ufd3f', u'\ufe18', u'\ufe36',
    u'\ufe38', u'\ufe3a', u'\ufe3c', u'\ufe3e', u'\ufe40', u'\ufe42', u'\ufe44',
    u'\ufe48', u'\ufe5a', u'\ufe5c', u'\ufe5e', u'\uff09', u'\uff3d', u'\uff5d',
    u'\uff60', u'\uff63']

open_punctuation = [u'(', u'[', u'{', u'\u0f3a', u'\u0f3c', u'\u169b',
    u'\u201a', u'\u201e', u'\u2045', u'\u207d', u'\u208d', u'\u2329', u'\u2768',
    u'\u276a', u'\u276c', u'\u276e', u'\u2770', u'\u2772', u'\u2774', u'\u27c5',
    u'\u27e6', u'\u27e8', u'\u27ea', u'\u27ec', u'\u27ee', u'\u2983', u'\u2985',
    u'\u2987', u'\u2989', u'\u298b', u'\u298d', u'\u298f', u'\u2991', u'\u2993',
    u'\u2995', u'\u2997', u'\u29d8', u'\u29da', u'\u29fc', u'\u2e22', u'\u2e24',
    u'\u2e26', u'\u2e28', u'\u3008', u'\u300a', u'\u300c', u'\u300e', u'\u3010',
    u'\u3014', u'\u3016', u'\u3018', u'\u301a', u'\u301d', u'\ufd3e', u'\ufe17',
    u'\ufe35', u'\ufe37', u'\ufe39', u'\ufe3b', u'\ufe3d', u'\ufe3f', u'\ufe41',
    u'\ufe43', u'\ufe47', u'\ufe59', u'\ufe5b', u'\ufe5d', u'\uff08', u'\uff3b',
    u'\uff5b', u'\uff5f', u'\uff62']

is_sc = currency_symbol = [u'$', u'\xa2', u'\xa3', u'\xa4', u'\xa5', u'\u058f',
    u'\u060b', u'\u09f2', u'\u09f3', u'\u09fb', u'\u0af1', u'\u0bf9', u'\u0e3f',
    u'\u17db', u'\u20a0', u'\u20a1', u'\u20a2', u'\u20a3', u'\u20a4', u'\u20a5',
    u'\u20a6', u'\u20a7', u'\u20a8', u'\u20a9', u'\u20aa', u'\u20ab', u'\u20ac',
    u'\u20ad', u'\u20ae', u'\u20af', u'\u20b0', u'\u20b1', u'\u20b2', u'\u20b3',
    u'\u20b4', u'\u20b5', u'\u20b6', u'\u20b7', u'\u20b8', u'\u20b9', u'\u20ba',
    u'\ua838', u'\ufdfc', u'\ufe69', u'\uff04', u'\uffe0', u'\uffe1', u'\uffe5',
    u'\uffe6']

with io.open(perluniprops_dir+'IsSo.txt', 'r', encoding='utf8') as fin:
    is_so = list(fin.read())

with io.open(perluniprops_dir+'IsAlpha.txt', 'r', encoding='utf8') as fin:
    is_alpha = list(fin.read())

with io.open(perluniprops_dir+'IsAlnum.txt', 'r', encoding='utf8') as fin:
    is_alnum = list(fin.read())

with io.open(perluniprops_dir+'IsLower.txt', 'r', encoding='utf8') as fin:
    is_lower = list(fin.read())

with io.open(perluniprops_dir+'IsUpper.txt', 'r', encoding='utf8') as fin:
    is_upper = list(fin.read())

is_n = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'\xb2',
    u'\xb3', u'\xb9', u'\xbc', u'\xbd', u'\xbe', u'\u0660', u'\u0661', u'\u0662',
    u'\u0663', u'\u0664', u'\u0665', u'\u0666', u'\u0667', u'\u0668', u'\u0669',
    u'\u06f0', u'\u06f1', u'\u06f2', u'\u06f3', u'\u06f4', u'\u06f5', u'\u06f6',
    u'\u06f7', u'\u06f8', u'\u06f9', u'\u07c0', u'\u07c1', u'\u07c2', u'\u07c3',
    u'\u07c4', u'\u07c5', u'\u07c6', u'\u07c7', u'\u07c8', u'\u07c9', u'\u0966',
    u'\u0967', u'\u0968', u'\u0969', u'\u096a', u'\u096b', u'\u096c', u'\u096d',
    u'\u096e', u'\u096f', u'\u09e6', u'\u09e7', u'\u09e8', u'\u09e9', u'\u09ea',
    u'\u09eb', u'\u09ec', u'\u09ed', u'\u09ee', u'\u09ef', u'\u09f4', u'\u09f5',
    u'\u09f6', u'\u09f7', u'\u09f8', u'\u09f9', u'\u0a66', u'\u0a67', u'\u0a68',
    u'\u0a69', u'\u0a6a', u'\u0a6b', u'\u0a6c', u'\u0a6d', u'\u0a6e', u'\u0a6f',
    u'\u0ae6', u'\u0ae7', u'\u0ae8', u'\u0ae9', u'\u0aea', u'\u0aeb', u'\u0aec',
    u'\u0aed', u'\u0aee', u'\u0aef', u'\u0b66', u'\u0b67', u'\u0b68', u'\u0b69',
    u'\u0b6a', u'\u0b6b', u'\u0b6c', u'\u0b6d', u'\u0b6e', u'\u0b6f', u'\u0b72',
    u'\u0b73', u'\u0b74', u'\u0b75', u'\u0b76', u'\u0b77', u'\u0be6', u'\u0be7',
    u'\u0be8', u'\u0be9', u'\u0bea', u'\u0beb', u'\u0bec', u'\u0bed', u'\u0bee',
    u'\u0bef', u'\u0bf0', u'\u0bf1', u'\u0bf2', u'\u0c66', u'\u0c67', u'\u0c68',
    u'\u0c69', u'\u0c6a', u'\u0c6b', u'\u0c6c', u'\u0c6d', u'\u0c6e', u'\u0c6f',
    u'\u0c78', u'\u0c79', u'\u0c7a', u'\u0c7b', u'\u0c7c', u'\u0c7d', u'\u0c7e',
    u'\u0ce6', u'\u0ce7', u'\u0ce8', u'\u0ce9', u'\u0cea', u'\u0ceb', u'\u0cec',
    u'\u0ced', u'\u0cee', u'\u0cef', u'\u0d66', u'\u0d67', u'\u0d68', u'\u0d69',
    u'\u0d6a', u'\u0d6b', u'\u0d6c', u'\u0d6d', u'\u0d6e', u'\u0d6f', u'\u0d70',
    u'\u0d71', u'\u0d72', u'\u0d73', u'\u0d74', u'\u0d75', u'\u0e50', u'\u0e51',
    u'\u0e52', u'\u0e53', u'\u0e54', u'\u0e55', u'\u0e56', u'\u0e57', u'\u0e58',
    u'\u0e59', u'\u0ed0', u'\u0ed1', u'\u0ed2', u'\u0ed3', u'\u0ed4', u'\u0ed5',
    u'\u0ed6', u'\u0ed7', u'\u0ed8', u'\u0ed9', u'\u0f20', u'\u0f21', u'\u0f22',
    u'\u0f23', u'\u0f24', u'\u0f25', u'\u0f26', u'\u0f27', u'\u0f28', u'\u0f29',
    u'\u0f2a', u'\u0f2b', u'\u0f2c', u'\u0f2d', u'\u0f2e', u'\u0f2f', u'\u0f30',
    u'\u0f31', u'\u0f32', u'\u0f33', u'\u1040', u'\u1041', u'\u1042', u'\u1043',
    u'\u1044', u'\u1045', u'\u1046', u'\u1047', u'\u1048', u'\u1049', u'\u1090',
    u'\u1091', u'\u1092', u'\u1093', u'\u1094', u'\u1095', u'\u1096', u'\u1097',
    u'\u1098', u'\u1099', u'\u1369', u'\u136a', u'\u136b', u'\u136c', u'\u136d',
    u'\u136e', u'\u136f', u'\u1370', u'\u1371', u'\u1372', u'\u1373', u'\u1374',
    u'\u1375', u'\u1376', u'\u1377', u'\u1378', u'\u1379', u'\u137a', u'\u137b',
    u'\u137c', u'\u16ee', u'\u16ef', u'\u16f0', u'\u17e0', u'\u17e1', u'\u17e2',
    u'\u17e3', u'\u17e4', u'\u17e5', u'\u17e6', u'\u17e7', u'\u17e8', u'\u17e9',
    u'\u17f0', u'\u17f1', u'\u17f2', u'\u17f3', u'\u17f4', u'\u17f5', u'\u17f6',
    u'\u17f7', u'\u17f8', u'\u17f9', u'\u1810', u'\u1811', u'\u1812', u'\u1813',
    u'\u1814', u'\u1815', u'\u1816', u'\u1817', u'\u1818', u'\u1819', u'\u1946',
    u'\u1947', u'\u1948', u'\u1949', u'\u194a', u'\u194b', u'\u194c', u'\u194d',
    u'\u194e', u'\u194f', u'\u19d0', u'\u19d1', u'\u19d2', u'\u19d3', u'\u19d4',
    u'\u19d5', u'\u19d6', u'\u19d7', u'\u19d8', u'\u19d9', u'\u19da', u'\u1a80',
    u'\u1a81', u'\u1a82', u'\u1a83', u'\u1a84', u'\u1a85', u'\u1a86', u'\u1a87',
    u'\u1a88', u'\u1a89', u'\u1a90', u'\u1a91', u'\u1a92', u'\u1a93', u'\u1a94',
    u'\u1a95', u'\u1a96', u'\u1a97', u'\u1a98', u'\u1a99', u'\u1b50', u'\u1b51',
    u'\u1b52', u'\u1b53', u'\u1b54', u'\u1b55', u'\u1b56', u'\u1b57', u'\u1b58',
    u'\u1b59', u'\u1bb0', u'\u1bb1', u'\u1bb2', u'\u1bb3', u'\u1bb4', u'\u1bb5',
    u'\u1bb6', u'\u1bb7', u'\u1bb8', u'\u1bb9', u'\u1c40', u'\u1c41', u'\u1c42',
    u'\u1c43', u'\u1c44', u'\u1c45', u'\u1c46', u'\u1c47', u'\u1c48', u'\u1c49',
    u'\u1c50', u'\u1c51', u'\u1c52', u'\u1c53', u'\u1c54', u'\u1c55', u'\u1c56',
    u'\u1c57', u'\u1c58', u'\u1c59', u'\u2070', u'\u2074', u'\u2075', u'\u2076',
    u'\u2077', u'\u2078', u'\u2079', u'\u2080', u'\u2081', u'\u2082', u'\u2083',
    u'\u2084', u'\u2085', u'\u2086', u'\u2087', u'\u2088', u'\u2089', u'\u2150',
    u'\u2151', u'\u2152', u'\u2153', u'\u2154', u'\u2155', u'\u2156', u'\u2157',
    u'\u2158', u'\u2159', u'\u215a', u'\u215b', u'\u215c', u'\u215d', u'\u215e',
    u'\u215f', u'\u2160', u'\u2161', u'\u2162', u'\u2163', u'\u2164', u'\u2165',
    u'\u2166', u'\u2167', u'\u2168', u'\u2169', u'\u216a', u'\u216b', u'\u216c',
    u'\u216d', u'\u216e', u'\u216f', u'\u2170', u'\u2171', u'\u2172', u'\u2173',
    u'\u2174', u'\u2175', u'\u2176', u'\u2177', u'\u2178', u'\u2179', u'\u217a',
    u'\u217b', u'\u217c', u'\u217d', u'\u217e', u'\u217f', u'\u2180', u'\u2181',
    u'\u2182', u'\u2185', u'\u2186', u'\u2187', u'\u2188', u'\u2189', u'\u2460',
    u'\u2461', u'\u2462', u'\u2463', u'\u2464', u'\u2465', u'\u2466', u'\u2467',
    u'\u2468', u'\u2469', u'\u246a', u'\u246b', u'\u246c', u'\u246d', u'\u246e',
    u'\u246f', u'\u2470', u'\u2471', u'\u2472', u'\u2473', u'\u2474', u'\u2475',
    u'\u2476', u'\u2477', u'\u2478', u'\u2479', u'\u247a', u'\u247b', u'\u247c',
    u'\u247d', u'\u247e', u'\u247f', u'\u2480', u'\u2481', u'\u2482', u'\u2483',
    u'\u2484', u'\u2485', u'\u2486', u'\u2487', u'\u2488', u'\u2489', u'\u248a',
    u'\u248b', u'\u248c', u'\u248d', u'\u248e', u'\u248f', u'\u2490', u'\u2491',
    u'\u2492', u'\u2493', u'\u2494', u'\u2495', u'\u2496', u'\u2497', u'\u2498',
    u'\u2499', u'\u249a', u'\u249b', u'\u24ea', u'\u24eb', u'\u24ec', u'\u24ed',
    u'\u24ee', u'\u24ef', u'\u24f0', u'\u24f1', u'\u24f2', u'\u24f3', u'\u24f4',
    u'\u24f5', u'\u24f6', u'\u24f7', u'\u24f8', u'\u24f9', u'\u24fa', u'\u24fb',
    u'\u24fc', u'\u24fd', u'\u24fe', u'\u24ff', u'\u2776', u'\u2777', u'\u2778',
    u'\u2779', u'\u277a', u'\u277b', u'\u277c', u'\u277d', u'\u277e', u'\u277f',
    u'\u2780', u'\u2781', u'\u2782', u'\u2783', u'\u2784', u'\u2785', u'\u2786',
    u'\u2787', u'\u2788', u'\u2789', u'\u278a', u'\u278b', u'\u278c', u'\u278d',
    u'\u278e', u'\u278f', u'\u2790', u'\u2791', u'\u2792', u'\u2793', u'\u2cfd',
    u'\u3192', u'\u3193', u'\u3194', u'\u3195', u'\u3220', u'\u3221', u'\u3222',
    u'\u3223', u'\u3224', u'\u3225', u'\u3226', u'\u3227', u'\u3228', u'\u3229',
    u'\u3248', u'\u3249', u'\u324a', u'\u324b', u'\u324c', u'\u324d', u'\u324e',
    u'\u324f', u'\u3251', u'\u3252', u'\u3253', u'\u3254', u'\u3255', u'\u3256',
    u'\u3257', u'\u3258', u'\u3259', u'\u325a', u'\u325b', u'\u325c', u'\u325d',
    u'\u325e', u'\u325f', u'\u3280', u'\u3281', u'\u3282', u'\u3283', u'\u3284',
    u'\u3285', u'\u3286', u'\u3287', u'\u3288', u'\u3289', u'\u32b1', u'\u32b2',
    u'\u32b3', u'\u32b4', u'\u32b5', u'\u32b6', u'\u32b7', u'\u32b8', u'\u32b9',
    u'\u32ba', u'\u32bb', u'\u32bc', u'\u32bd', u'\u32be', u'\u32bf', u'\ua620',
    u'\ua621', u'\ua622', u'\ua623', u'\ua624', u'\ua625', u'\ua626', u'\ua627',
    u'\ua628', u'\ua629', u'\ua6e6', u'\ua6e7', u'\ua6e8', u'\ua6e9', u'\ua6ea',
    u'\ua6eb', u'\ua6ec', u'\ua6ed', u'\ua6ee', u'\ua6ef', u'\ua830', u'\ua831',
    u'\ua832', u'\ua833', u'\ua834', u'\ua835', u'\ua8d0', u'\ua8d1', u'\ua8d2',
    u'\ua8d3', u'\ua8d4', u'\ua8d5', u'\ua8d6', u'\ua8d7', u'\ua8d8', u'\ua8d9',
    u'\ua900', u'\ua901', u'\ua902', u'\ua903', u'\ua904', u'\ua905', u'\ua906',
    u'\ua907', u'\ua908', u'\ua909', u'\ua9d0', u'\ua9d1', u'\ua9d2', u'\ua9d3',
    u'\ua9d4', u'\ua9d5', u'\ua9d6', u'\ua9d7', u'\ua9d8', u'\ua9d9', u'\uaa50',
    u'\uaa51', u'\uaa52', u'\uaa53', u'\uaa54', u'\uaa55', u'\uaa56', u'\uaa57',
    u'\uaa58', u'\uaa59', u'\uabf0', u'\uabf1', u'\uabf2', u'\uabf3', u'\uabf4',
    u'\uabf5', u'\uabf6', u'\uabf7', u'\uabf8', u'\uabf9', u'\uff10', u'\uff11',
    u'\uff12', u'\uff13', u'\uff14', u'\uff15', u'\uff16', u'\uff17', u'\uff18',
    u'\uff19']

# Shield the top level imports from all the local variables.
__all__ = ['close_punctuation', 'open_punctuation', 'currency_symbol',
           'is_sc', 'is_alnum', 'is_alpha', 'is_lower', 'is_upper', 'is_n', 'is_so']
