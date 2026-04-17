# -*- coding: utf-8 -*-

"""
Vietnamese Character Vommitting.
See http://www.wazu.jp/gallery/Test_Vietnamese.html
and https://www.tug.org/TUGboat/tb24-1/thanh.pdf
Perhaps, see also:
https://www.reddit.com/r/learnvietnamese/comments/2xml9o/is_there_any_way_to_type_in_vietnamese_on_the/
and http://typingvietnamese.blogspot.sg/p/keystrokes-telex-vni-viqr.html
"""

import re
from itertools import chain
from collections import namedtuple

VietTone = namedtuple('Tones', 'ngang huyen sac hoi nga nang')

viet_tones = VietTone(ngang='',       # mid level
                      sac='\u0301',   # high rising
                      huyen='\u0300', # low falling
                      hoi='\u0309',   # mid dipping-rising
                      nga='\u0303',   # high breaking-rising
                      nang='\u0323'   # low falling constricted
                     )

# A vowels
upper_a_ngang = 'A'
upper_a_sac = '\u00c1'     # 'Á'
upper_a_huyen = '\u00c0'   # 'À'
upper_a_hoi = '\u1ea2'     # 'Ả'
upper_a_nga = '\u00c3'     # 'Ã'
upper_a_nang = '\u1ea0'    # 'Ạ'
# a vowels
lower_a_ngang = 'a'
lower_a_sac = '\u00e1'     # 'á'
lower_a_huyen = '\u00e0'   # 'à'
lower_a_hoi = '\u1ea3'     # 'ả'
lower_a_nga = '\u00e3'     # 'ã'
lower_a_nang = '\u1ea1'    # 'ạ'
# A8 vowels (Telex: Aw)
upper_abreve_ngang = '\u0102'   # 'Ă'
upper_abreve_sac = '\u1eae'     # 'Ắ'
upper_abreve_huyen = '\u1eb0'   # 'Ằ'
upper_abreve_hoi = '\u1eb2'     # 'Ẳ'
upper_abreve_nga = '\u1eb4'     # 'Ẵ'
upper_abreve_nang = '\u1eb6'    # 'Ặ'
# a8 vowels (Telex: aa)
lower_abreve_ngang = '\u0103'   # 'ă'
lower_abreve_sac = '\u1eaf'     # 'ắ'
lower_abreve_huyen = '\u1eb1'   # 'ằ'
lower_abreve_hoi = '\u1eb3'     # 'ẳ'
lower_abreve_nga = '\u1eb5'     # 'ẵ'
lower_abreve_nang = '\u1eb7'    # 'ặ'
# A6 vowels (Telex: Aa)
upper_ahat_ngang = '\u00c2'   # 'Â'
upper_ahat_sac = '\u1ea4'     # 'Ấ'
upper_ahat_huyen = '\u1ea6'   # 'Ầ'
upper_ahat_hoi = '\u1ea8'     # 'Ẩ'
upper_ahat_nga = '\u1eaa'     # 'Ẫ'
upper_ahat_nang = '\u1eac'    # 'Ậ'
# a6 vowels (Telex: aa)
lower_ahat_ngang = '\u00e2'   # 'â'
lower_ahat_sac = '\u1ea5'     # 'ấ'
lower_ahat_huyen = '\u1ea7'   # 'ầ'
lower_ahat_hoi = '\u1ea9'     # 'ẩ'
lower_ahat_nga = '\u1eab'     # 'ẫ'
lower_ahat_nang = '\u1ead'    # 'ậ'

# E vowels
upper_e_ngang = 'E'
upper_e_sac = '\u00c9'     # 'É'
upper_e_huyen = '\u00c8'   # 'È'
upper_e_hoi = '\u1eba'     # 'Ẻ'
upper_e_nga = '\u1ebc'     # 'Ẽ'
upper_e_nang = '\u1eb8'    # 'Ẹ'
# e vowels
lower_e_ngang = 'e'
lower_e_sac = '\u00e9'     # 'é'
lower_e_huyen = '\u00e8'   # 'è'
lower_e_hoi = '\u1ebb'     # 'ẻ'
lower_e_nga = '\u1ebd'     # 'ẽ'
lower_e_nang = '\u1eb9'    # 'ẹ'
# E6 vowels (TELEX: Ee)
upper_ehat_ngang = '\u00ca'   # 'Ê'
upper_ehat_sac = '\u1ebe'     # 'Ế'
upper_ehat_huyen = '\u1ec0'   # 'Ề'
upper_ehat_hoi = '\u1ec2'     # 'Ể'
upper_ehat_nga = '\u1ec4'     # 'Ễ'
upper_ehat_nang = '\u1ec6'    # 'Ệ'
# e6 vowels (TELEX: ee)
lower_ehat_ngang = '\u00ea'   # 'ê'
lower_ehat_sac = '\u1ebf'     # 'ế'
lower_ehat_huyen = '\u1ec1'   # 'ề'
lower_ehat_hoi = '\u1ec3'     # 'ể'
lower_ehat_nga = '\u1ec5'     # 'ễ'
lower_ehat_nang = '\u1ec7'    # 'ệ'

# I vowels
upper_i_ngang = 'I'
upper_i_sac = '\u00cd'        # 'Í'
upper_i_huyen = '\u00cc'      # 'Ì'
upper_i_hoi = '\u1ec8'        # 'Ỉ'
upper_i_nga = '\u0128'        # 'Ĩ'
upper_i_nang = '\u1eca'       # 'Ị'
# i vowels
lower_i_ngang = 'i'
lower_i_sac = '\u00ed'        # 'í'
lower_i_huyen = '\u00ec'      # 'ì'
lower_i_hoi = '\u1ec9'        # 'ỉ'
lower_i_nga = '\u0129'        # 'ĩ'
lower_i_nang = '\u1ecb'       # 'ị'

# O vowels
upper_o_ngang = 'O'
upper_o_sac = '\u00d3'     # 'Ó'
upper_o_huyen = '\u00d2'   # 'Ò'
upper_o_hoi = '\u1ece'     # 'Ỏ'
upper_o_nga = '\u1ed5'     # 'Õ'
upper_o_nang = '\u1ecc'    # 'Ọ'
# o vowels
lower_o_ngang = 'o'
lower_o_sac = '\u00f3'     # 'ó'
lower_o_huyen = '\u00f2'   # 'ò'
lower_o_hoi = '\u1ecf'     # 'ỏ'
lower_o_nga = '\u00f5'     # 'õ'
lower_o_nang = '\u1ecd'    # 'ọ'

# O6 vowels (TELEX: Oo)
upper_ohat_ngang = '\u00d4'   # 'Ô'
upper_ohat_sac = '\u1ed0'     # 'Ố'
upper_ohat_huyen = '\u1ed2'   # 'Ồ'
upper_ohat_hoi = '\u1ed4'     # 'Ổ'
upper_ohat_nga = '\u1ed6'     # 'Ỗ'
upper_ohat_nang = '\u1ed8'    # 'Ộ'
# o6 vowels (TELEX: oo)
lower_ohat_ngang = '\u00f4'   # 'ô'
lower_ohat_sac = '\u1ed1'     # 'ố'
lower_ohat_huyen = '\u1ed3'   # 'ồ'
lower_ohat_hoi = '\u1ed5'     # 'ổ'
lower_ohat_nga = '\u1ed7'     # 'ỗ'
lower_ohat_nang = '\u1ed9'    # 'ộ'
# O7  vowels (TELEX: Ow)
upper_oplus_ngang = '\u01a0'  # 'Ơ'
upper_oplus_sac = '\u1eda'    # 'Ớ'
upper_oplus_huyen = '\u1edc'  # 'Ờ'
upper_oplus_hoi = '\u1ede'    # 'Ở'
upper_oplus_nga = '\u1ee0'    # 'Ỡ'
upper_oplus_nang = '\u1ee2'   # 'Ợ'
# o7  vowels (TELEX: Ow)
lower_oplus_ngang = '\u01a1'  # ơ
lower_oplus_sac = '\u1edb'    # 'ớ'
lower_oplus_huyen = '\u1edd'  # 'ờ'
lower_oplus_hoi = '\u1edf'    # 'ở'
lower_oplus_nga = '\u1ee1'    # 'ỡ'
lower_oplus_nang = '\u1ee3'   # 'ợ'

# U vowels
upper_u_ngang = 'U'
upper_u_sac = '\u00da'       # 'Ú'
upper_u_huyen = '\u00d9'     # 'Ù'
upper_u_hoi = '\u1ee6'       # 'Ủ'
upper_u_nga = '\u0168'       # 'ũ'
upper_u_nang = '\u1ee4'      # 'Ụ'
# u vowels
lower_u_ngang = 'u'
lower_u_sac = '\u00fa'       # 'ú'
lower_u_huyen = '\u00f9'     # 'ù'
lower_u_hoi = '\u1ee7'       # 'ủ'
lower_u_nga = '\u0169'       # 'ũ'
lower_u_nang = '\u1ee5'      # 'ụ'
# U7 vowels (TELEX: Uw)
upper_uplus_ngang = '\u01af' # 'Ư'
upper_uplus_sac = '\u1ee8'   # 'Ừ'
upper_uplus_huyen = '\u1eea' # 'Ứ'
upper_uplus_hoi = '\u1eec'   # 'Ử'
upper_uplus_nga = '\u1eee'   # 'Ữ'
upper_uplus_nang = '\u1ef0'  # 'Ự'
# u7 vowels (TELEX: uw)
lower_uplus_ngang = '\u01b0' # 'ư'
lower_uplus_sac = '\u1ee9'   # 'ừ'
lower_uplus_huyen = '\u1eeb' # 'ứ'
lower_uplus_hoi = '\u1eed'   # 'ử'
lower_uplus_nga = '\u1eef'   # 'ữ'
lower_uplus_nang = '\u1ef1'  # 'ự'

# Y vowels
upper_y_ngang = 'Y'
upper_y_sac = '\u00dd'   # 'Ý'
upper_y_huyen = '\u1ef2' # 'Ỳ'
upper_y_hoi = '\u1ef6'   # 'Ỷ'
upper_y_nga = '\u1ef8'   # 'Ỹ'
upper_y_nang = '\u1ef4'  # 'Ỵ'
# y vowels
lower_y_ngang = 'y'
lower_y_sac = '\u00fd'   # 'ý'
lower_y_huyen = '\u1ef3' # 'ỳ'
lower_y_hoi = '\u1ef7'   # 'ỷ'
lower_y_nga = '\u1ef9'   # 'ỹ'
lower_y_nang = '\u1ef5'  # 'ỵ'

a = [upper_a_ngang, upper_a_sac, upper_a_huyen,
     upper_a_hoi, upper_a_nga, upper_a_nang,
     lower_a_ngang, lower_a_sac, lower_a_huyen,
     lower_a_hoi, lower_a_nga, lower_a_nang]

a8 = [upper_abreve_ngang, upper_abreve_sac, upper_abreve_huyen,
      upper_abreve_hoi, upper_abreve_nga, upper_abreve_nang,
      lower_abreve_ngang, lower_abreve_sac, lower_abreve_huyen,
      lower_abreve_hoi, lower_abreve_nga, lower_abreve_nang]

a6 = [upper_ahat_ngang, upper_ahat_sac, upper_ahat_huyen,
      upper_ahat_hoi, upper_ahat_nga, upper_ahat_nang,
      lower_ahat_ngang, lower_ahat_sac, lower_ahat_huyen,
      lower_ahat_hoi, lower_ahat_nga, lower_ahat_nang]

e = [upper_e_ngang, upper_e_sac, upper_e_huyen,
     upper_e_hoi, upper_e_nga, upper_e_nang,
     lower_e_ngang, lower_e_sac, lower_e_huyen,
     lower_e_hoi, lower_e_nga, lower_e_nang]

e6 = [upper_ehat_ngang, upper_ehat_sac, upper_ehat_huyen,
      upper_ehat_hoi, upper_ehat_nga, upper_ehat_nang,
      lower_ehat_ngang, lower_ehat_sac, lower_ehat_huyen,
      lower_ehat_hoi, lower_ehat_nga, lower_ehat_nang]

i = [upper_i_ngang, upper_i_sac, upper_i_huyen,
     upper_i_hoi, upper_i_nga, upper_i_nang,
     lower_i_ngang, lower_i_sac, lower_i_huyen,
     lower_i_hoi, lower_i_nga, lower_i_nang]

o = [upper_o_ngang, upper_o_sac, upper_o_huyen,
     upper_o_hoi, upper_o_nga, upper_o_nang,
     lower_o_ngang, lower_o_sac, lower_o_huyen,
     lower_o_hoi, lower_o_nga, lower_o_nang]

o6 = [upper_ohat_ngang, upper_ohat_sac, upper_ohat_huyen,
      upper_ohat_hoi, upper_ohat_nga, upper_ohat_nang,
      lower_ohat_ngang, lower_ohat_sac, lower_ohat_huyen,
      lower_ohat_hoi, lower_ohat_nga, lower_ohat_nang]

o7 = [upper_oplus_ngang, upper_oplus_sac, upper_oplus_huyen,
      upper_oplus_hoi, upper_oplus_nga, upper_oplus_nang,
      lower_oplus_ngang, lower_oplus_sac, lower_oplus_huyen,
      lower_oplus_hoi, lower_oplus_nga, lower_oplus_nang]

u = [upper_u_ngang, upper_u_sac, upper_u_huyen,
     upper_u_hoi, upper_u_nga, upper_u_nang,
     lower_u_ngang, lower_u_sac, lower_u_huyen,
     lower_u_hoi, lower_u_nga, lower_u_nang]

u7 = [upper_uplus_ngang, upper_uplus_sac, upper_uplus_huyen,
      upper_uplus_hoi, upper_uplus_nga, upper_uplus_nang,
      lower_uplus_ngang, lower_uplus_sac, lower_uplus_huyen,
      lower_uplus_hoi, lower_uplus_nga, lower_uplus_nang]

y = [upper_y_ngang, upper_y_sac, upper_y_huyen,
     upper_y_hoi, upper_y_nga, upper_y_nang,
     lower_y_ngang, lower_y_sac, lower_y_huyen,
     lower_y_hoi, lower_y_nga, lower_y_nang]

viet_consonants_upper = ['A', 'Ă', 'Â', 'B', 'C', 'Ch', 'D', 'Đ',
                         'E', 'Ê', 'G', 'Gh', 'Gi', 'H', 'I',
                         'K', 'Kh', 'L', 'M', 'N', 'Ng', 'Ngh', 'Nh',
                         'O', 'Ô', 'Ơ', 'P', 'Ph', 'Q', 'R',
                         'S', 'T', 'Th', 'Tr', 'U', 'Ư', 'V',
                         'X', 'Y', 'F', 'J', 'W', 'Z']

viet_consonants_lower = ['a', 'ă', 'â', 'b', 'c', 'ch', 'd', 'đ',
                         'e', 'ê', 'g', 'gh', 'gi', 'h', 'i',
                         'k', 'kh', 'l', 'm', 'n', 'ng', 'ngh', 'nh',
                         'o', 'ô', 'ơ', 'p', 'ph', 'q', 'r',
                         's', 't', 'th', 'tr', 'u', 'ư', 'v',
                         'x', 'y', 'f', 'j', 'w', 'z']

viet_consonants = viet_consonants_upper + viet_consonants_lower
viet_vowels = list(chain(*[a, a8, a6, e, e6, i, o, o6, o7, u, u7, y]))
viet_utf8 = viet_consonants + viet_vowels

vni_mappings = {'A8':a8[0], 'A81':a8[1], 'A82':a8[2], 'A83':a8[3], 'A84':a8[4],  'A85':a8[5],
                'a8':a8[6], 'a81':a8[7], 'a82':a8[8], 'a83':a8[9], 'a84':a8[10], 'a85':a8[11],
                'A6':a6[0], 'A61':a6[1], 'A62':a6[2], 'A63':a6[3], 'A64':a6[4],  'A65':a6[5],
                'a6':a6[6], 'a61':a6[7], 'a62':a6[8], 'a63':a6[9], 'a64':a6[10], 'a65':a6[11],
                'E6':e6[0], 'E61':e6[1], 'E62':e6[2], 'E63':e6[3], 'E64':e6[4],  'E65':e6[5],
                'e6':e6[6], 'e61':e6[7], 'e62':e6[8], 'e63':e6[9], 'e64':e6[10], 'e65':e6[11],
                'O6':o6[0], 'O61':o6[1], 'O62':o6[2], 'O63':o6[3], 'O64':o6[4],  'O65':o6[5],
                'o6':o6[6], 'o61':o6[7], 'o62':o6[8], 'o63':o6[9], 'o64':o6[10], 'o65':o6[11],
                'O7':o7[0], 'O71':o7[1], 'O72':o7[2], 'O73':o7[3], 'O74':o7[4],  'O75':o7[5],
                'o7':o7[6], 'o71':o7[7], 'o72':o7[8], 'o73':o7[9], 'o74':o7[10], 'o75':o7[11],
                'U7':u7[0], 'U71':u7[1], 'U72':u7[2], 'U73':u7[3], 'U74':u7[4],  'U75':u7[5],
                'u7':u7[6], 'u71':u7[7], 'u72':u7[8], 'u73':u7[9], 'u74':u7[10], 'u75':u7[11],
                'D9': 'Đ', 'd9': 'đ',
                'A1':a[1], 'A2':a[2], 'A3':a[3], 'A4':a[4],  'A5':a[5],
                'a1':a[7], 'a2':a[8], 'a3':a[9], 'a4':a[10], 'a5':a[11],
                'E1':e[1], 'E2':e[2], 'E3':e[3], 'E4':e[4],  'E5':e[5],
                'e1':e[7], 'e2':e[8], 'e3':e[9], 'e4':e[10], 'e5':e[11],
                'I1':i[1], 'I2':i[2], 'I3':i[3], 'I4':i[4],  'I5':i[5],
                'i1':i[7], 'i2':i[8], 'i3':i[9], 'i4':i[10], 'i5':i[11],
                'O1':o[1], 'O2':o[2], 'O3':o[3], 'O4':o[4],  'O5':o[5],
                'o1':o[7], 'o2':o[8], 'o3':o[9], 'o4':o[10], 'o5':o[11],
                'U1':u[1], 'U2':u[2], 'U3':u[3], 'U4':u[4],  'U5':u[5],
                'u1':u[7], 'u2':u[8], 'u3':u[9], 'u4':u[10], 'u5':u[11],
                }


telex_mappings = {'Aw':a8[0], 'Aws':a8[1], 'Awf':a8[2], 'Awr':a8[3], 'Awx':a8[4],  'Awj':a8[5],
                  'aw':a8[6], 'aws':a8[7], 'awf':a8[8], 'awr':a8[9], 'awx':a8[10], 'awj':a8[11],
                  'Aa':a6[0], 'Aas':a6[1], 'Aaf':a6[2], 'Aar':a6[3], 'Aax':a6[4],  'Aaj':a6[5],
                  'aa':a6[6], 'aas':a6[7], 'aaf':a6[8], 'aar':a6[9], 'aax':a6[10], 'aaj':a6[11],
                  'Ee':e6[0], 'Ees':e6[1], 'Eef':e6[2], 'Eer':e6[3], 'Eex':e6[4],  'Eej':e6[5],
                  'ee':e6[6], 'ees':e6[7], 'eef':e6[8], 'eer':e6[9], 'eex':e6[10], 'eej':e6[11],
                  'Oo':o6[0], 'Oos':o6[1], 'Oof':o6[2], 'Oor':o6[3], 'Oox':o6[4],  'Ooj':o6[5],
                  'oo':o6[6], 'oos':o6[7], 'oof':o6[8], 'oor':o6[9], 'oox':o6[10], 'ooj':o6[11],
                  'Ow':o7[0], 'Ows':o7[1], 'Owf':o7[2], 'Owr':o7[3], 'Owx':o7[4],  'Owj':o7[5],
                  'ow':o7[6], 'ows':o7[7], 'owf':o7[8], 'owr':o7[9], 'owx':o7[10], 'owj':o7[11],
                  'Uw':u7[0], 'Uws':u7[1], 'Uwf':u7[2], 'Uwr':u7[3], 'Uwx':u7[4],  'Uwj':u7[5],
                  'uw':u7[6], 'uws':u7[7], 'uwf':u7[8], 'uwr':u7[9], 'uwx':u7[10], 'uwj':u7[11],
                  'Dd': 'Đ', 'dd': 'đ',
                  'As':a[1], 'Af':a[2], 'Ar':a[3], 'Ax':a[4],  'Aj':a[5],
                  'as':a[7], 'af':a[8], 'ar':a[9], 'ax':a[10], 'aj':a[11],
                  'Es':e[1], 'Ef':e[2], 'Er':e[3], 'Ex':e[4],  'Ej':e[5],
                  'es':e[7], 'ef':e[8], 'er':e[9], 'ex':e[10], 'ej':e[11],
                  'Is':i[1], 'If':i[2], 'Ir':i[3], 'Ix':i[4],  'Ij':i[5],
                  'is':i[7], 'if':i[8], 'ir':i[9], 'ix':i[10], 'ij':i[11],
                  'Os':o[1], 'Of':o[2], 'Or':o[3], 'Ox':o[4],  'Oj':o[5],
                  'os':o[7], 'of':o[8], 'or':o[9], 'ox':o[10], 'oj':o[11],
                  'Us':u[1], 'Uf':u[2], 'Ur':u[3], 'Ux':u[4],  'Uj':u[5],
                  'us':u[7], 'uf':u[8], 'ur':u[9], 'ux':u[10], 'uj':u[11],

                }

def viet_ime(s, mapping='vni', raise_keyerror=False):
    """Convert an input-method-encoded ASCII string ``s`` to Vietnamese.

    Parameters
    ----------
    s : str
        Text containing IME escapes (e.g. ``'Nguye64n'`` for VNI,
        ``'Nguyeefn'`` for Telex).
    mapping : {'vni', 'telex'}
        Which IME scheme to decode. VNI uses digit suffixes on a letter
        (``a1`` → ``á``, ``a62`` → ``ầ``); Telex uses letter pairs
        (``aa`` → ``â``, ``as`` → ``á``).
    raise_keyerror : bool
        VNI only. If True, an unknown escape like ``'u8'`` raises
        :class:`KeyError`. If False (default), unknown escapes pass through.

    Returns
    -------
    str
        The decoded text. Characters outside any escape are preserved.
    """
    if mapping == 'vni':
        _mapping = vni_mappings
        if raise_keyerror:
            return re.sub(r'[A-Za-z]\d+', lambda m: _mapping[m.group(0)], s)
        else:
            return re.sub(r'[A-Za-z]\d+', lambda m: _mapping.get(m.group(0), m.group(0)), s)
    elif mapping == 'telex':
        _mapping = telex_mappings
        _pattern = '|'.join(re.escape(word) for word in
                            sorted(_mapping, key=len, reverse=True))
        return re.sub(_pattern, lambda match: telex_mappings[match.group()], s)
    raise ValueError(f"mapping must be 'vni' or 'telex', got {mapping!r}")


# Shield the top level imports from all the local variables.
__all__ = ['viet_vowels', 'viet_consonants', 'viet_utf8', 'viet_tones',
           'vni_mappings', 'telex_mappings', 'viet_ime']
