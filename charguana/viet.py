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

viet_tones = VietTone(ngang=u'',       # mid level
                      sac=u'\u0301',   # high rising
                      huyen=u'\u0300', # low falling
                      hoi=u'\u0309',   # mid dipping-rising
                      nga=u'\u0303',   # high breaking-rising
                      nang=u'\u0323'   # low falling constricted
                     )

# A vowels
upper_a_ngang = u'A'
upper_a_sac = u'\u00c1'     # u'Á'
upper_a_huyen = u'\u00c0'   # u'À'
upper_a_hoi = u'\u1ea2'     # u'Ả'
upper_a_nga = u'\u00c3'     # u'Ã'
upper_a_nang = u'\u1ea0'    # u'Ạ'
# a vowels
lower_a_ngang = u'a'
lower_a_sac = u'\u00e1'     # u'á'
lower_a_huyen = u'\u00e0'   # u'à'
lower_a_hoi = u'\u1ea3'     # u'ả'
lower_a_nga = u'\u00e3'     # u'ã'
lower_a_nang = u'\u1ea1'    # u'ạ'
# A8 vowels (Telex: Aw)
upper_abreve_ngang = u'\u0102'   # u'Ă'
upper_abreve_sac = u'\u1eae'     # u'Ắ'
upper_abreve_huyen = u'\u1eb0'   # u'Ằ'
upper_abreve_hoi = u'\u1eb2'     # u'Ẳ'
upper_abreve_nga = u'\u1eb4'     # u'Ẵ'
upper_abreve_nang = u'\u1eb6'    # u'Ặ'
# a8 vowels (Telex: aa)
lower_abreve_ngang = u'\u0103'   # u'ă'
lower_abreve_sac = u'\u1eaf'     # u'ắ'
lower_abreve_huyen = u'\u1eb1'   # u'ằ'
lower_abreve_hoi = u'\u1eb3'     # u'ẳ'
lower_abreve_nga = u'\u1eb5'     # u'ẵ'
lower_abreve_nang = u'\u1eb7'    # u'ặ'
# A6 vowels (Telex: Aa)
upper_ahat_ngang = u'\u00c2'   # u'Â'
upper_ahat_sac = u'\u1ea4'     # u'Ấ'
upper_ahat_huyen = u'\u1ea6'   # u'Ầ'
upper_ahat_hoi = u'\u1ea8'     # u'Ẩ'
upper_ahat_nga = u'\u1eaa'     # u'Ẫ'
upper_ahat_nang = u'\u1eac'    # u'Ậ'
# a6 vowels (Telex: aa)
lower_ahat_ngang = u'\u00e2'   # u'â'
lower_ahat_sac = u'\u1ea5'     # u'ấ'
lower_ahat_huyen = u'\u1ea7'   # u'ầ'
lower_ahat_hoi = u'\u1ea9'     # u'ẩ'
lower_ahat_nga = u'\u1eab'     # u'ẫ'
lower_ahat_nang = u'\u1ead'    # u'ậ'

# E vowels
upper_e_ngang = u'E'
upper_e_sac = u'\u00c9'     # u'É'
upper_e_huyen = u'\u00c8'   # u'È'
upper_e_hoi = u'\u1eba'     # u'Ẻ'
upper_e_nga = u'\u1ebc'     # u'Ẽ'
upper_e_nang = u'\u1eb8'    # u'Ẹ'
# e vowels
lower_e_ngang = u'e'
lower_e_sac = u'\u00e9'     # u'é'
lower_e_huyen = u'\u00e8'   # u'è'
lower_e_hoi = u'\u1ebb'     # u'ẻ'
lower_e_nga = u'\u1ebd'     # u'ẽ'
lower_e_nang = u'\u1eb9'    # u'ẹ'
# E6 vowels (TELEX: Ee)
upper_ehat_ngang = u'\u00ca'   # u'Ê'
upper_ehat_sac = u'\u1ebe'     # u'Ế'
upper_ehat_huyen = u'\u1ec0'   # u'Ề'
upper_ehat_hoi = u'\u1ec2'     # u'Ể'
upper_ehat_nga = u'\u1ec4'     # u'Ễ'
upper_ehat_nang = u'\u1ec6'    # u'Ệ'
# e6 vowels (TELEX: ee)
lower_ehat_ngang = u'\u00ea'   # u'ê'
lower_ehat_sac = u'\u1ebf'     # u'ế'
lower_ehat_huyen = u'\u1ec1'   # u'ề'
lower_ehat_hoi = u'\u1ec3'     # u'ể'
lower_ehat_nga = u'\u1ec5'     # u'ễ'
lower_ehat_nang = u'\u1ec7'    # u'ệ'

# I vowels
upper_i_ngang = u'I'
upper_i_sac = u'\u00cd'        # u'Í'
upper_i_huyen = u'\u00cc'      # u'Ì'
upper_i_hoi = u'\u1ec8'        # u'Ỉ'
upper_i_nga = u'\u0128'        # u'Ĩ'
upper_i_nang = u'\u1eca'       # u'Ị'
# i vowels
lower_i_ngang = u'i'
lower_i_sac = u'\u00ed'        # u'í'
lower_i_huyen = u'\u00ec'      # u'ì'
lower_i_hoi = u'\u1ec9'        # u'ỉ'
lower_i_nga = u'\u0129'        # u'ĩ'
lower_i_nang = u'\u1ecb'       # u'ị'

# O vowels
upper_o_ngang = u'O'
upper_o_sac = u'\u00d3'     # u'Ó'
upper_o_huyen = u'\u00d2'   # u'Ò'
upper_o_hoi = u'\u1ece'     # u'Ỏ'
upper_o_nga = u'\u1ed5'     # u'Õ'
upper_o_nang = u'\u1ecc'    # u'Ọ'
# o vowels
lower_o_ngang = u'o'
lower_o_sac = u'\u00f3'     # u'ó'
lower_o_huyen = u'\u00f2'   # u'ò'
lower_o_hoi = u'\u1ecf'     # u'ỏ'
lower_o_nga = u'\u00f5'     # u'õ'
lower_o_nang = u'\u1ecd'    # u'ọ'

# O6 vowels (TELEX: Oo)
upper_ohat_ngang = u'\u00d4'   # u'Ô'
upper_ohat_sac = u'\u1ed0'     # u'Ố'
upper_ohat_huyen = u'\u1ed2'   # u'Ồ'
upper_ohat_hoi = u'\u1ed4'     # u'Ổ'
upper_ohat_nga = u'\u1ed6'     # u'Ỗ'
upper_ohat_nang = u'\u1ed8'    # u'Ộ'
# o6 vowels (TELEX: oo)
lower_ohat_ngang = u'\u00f4'   # u'ô'
lower_ohat_sac = u'\u1ed1'     # u'ố'
lower_ohat_huyen = u'\u1ed3'   # u'ồ'
lower_ohat_hoi = u'\u1ed5'     # u'ổ'
lower_ohat_nga = u'\u1ed7'     # u'ỗ'
lower_ohat_nang = u'\u1ed9'    # u'ộ'
# O7  vowels (TELEX: Ow)
upper_oplus_ngang = u'\u01a0'  # u'Ơ'
upper_oplus_sac = u'\u1eda'    # u'Ớ'
upper_oplus_huyen = u'\u1edc'  # u'Ờ'
upper_oplus_hoi = u'\u1ede'    # u'Ở'
upper_oplus_nga = u'\u1ee0'    # u'Ỡ'
upper_oplus_nang = u'\u1ee2'   # u'Ợ'
# o7  vowels (TELEX: Ow)
lower_oplus_ngang = u'\u01a1'  # ơ
lower_oplus_sac = u'\u1edb'    # u'ớ'
lower_oplus_huyen = u'\u1edd'  # u'ờ'
lower_oplus_hoi = u'\u1edf'    # u'ở'
lower_oplus_nga = u'\u1ee1'    # u'ỡ'
lower_oplus_nang = u'\u1ee3'   # u'ợ'

# U vowels
upper_u_ngang = u'U'
upper_u_sac = u'\u00da'       # u'Ú'
upper_u_huyen = u'\u00d9'     # u'Ù'
upper_u_hoi = u'\u1ee6'       # u'Ủ'
upper_u_nga = u'\u0168'       # u'ũ'
upper_u_nang = u'\u1ee4'      # u'Ụ'
# u vowels
lower_u_ngang = u'u'
lower_u_sac = u'\u00fa'       # u'ú'
lower_u_huyen = u'\u00f9'     # u'ù'
lower_u_hoi = u'\u1ee7'       # u'ủ'
lower_u_nga = u'\u0169'       # u'ũ'
lower_u_nang = u'\u1ee5'      # u'ụ'
# U7 vowels (TELEX: Uw)
upper_uplus_ngang = u'\u01af' # u'Ư'
upper_uplus_sac = u'\u1ee8'   # u'Ừ'
upper_uplus_huyen = u'\u1eea' # u'Ứ'
upper_uplus_hoi = u'\u1eec'   # u'Ử'
upper_uplus_nga = u'\u1eee'   # u'Ữ'
upper_uplus_nang = u'\u1ef0'  # u'Ự'
# u7 vowels (TELEX: uw)
lower_uplus_ngang = u'\u01b0' # u'ư'
lower_uplus_sac = u'\u1ee9'   # u'ừ'
lower_uplus_huyen = u'\u1eeb' # u'ứ'
lower_uplus_hoi = u'\u1eed'   # u'ử'
lower_uplus_nga = u'\u1eef'   # u'ữ'
lower_uplus_nang = u'\u1ef1'  # u'ự'

# Y vowels
upper_y_ngang = u'Y'
upper_y_sac = u'\u00dd'   # u'Ý'
upper_y_huyen = u'\u1ef2' # u'Ỳ'
upper_y_hoi = u'\u1ef6'   # u'Ỷ'
upper_y_nga = u'\u1ef8'   # u'Ỹ'
upper_y_nang = u'\u1ef4'  # u'Ỵ'
# y vowels
lower_y_ngang = u'y'
lower_y_sac = u'\u00fd'   # u'ý'
lower_y_huyen = u'\u1ef3' # u'ỳ'
lower_y_hoi = u'\u1ef7'   # u'ỷ'
lower_y_nga = u'\u1ef9'   # u'ỹ'
lower_y_nang = u'\u1ef5'  # u'ỵ'

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
     lower_u_hoi, upper_u_nga, upper_u_nang]

u7 = [upper_uplus_ngang, upper_uplus_sac, upper_uplus_huyen,
      upper_uplus_hoi, upper_uplus_nga, upper_uplus_nang,
      lower_uplus_ngang, lower_uplus_sac, lower_uplus_huyen,
      lower_uplus_hoi, lower_uplus_nga, lower_uplus_nang]

y = [upper_y_ngang, upper_y_sac, upper_y_huyen,
     upper_y_hoi, upper_y_nga, upper_y_nang,
     lower_y_ngang, lower_y_sac, lower_y_huyen,
     lower_y_hoi, lower_y_nga, lower_y_nang]

viet_consonants_upper = [u'A', u'Ă', u'Â', u'B', u'C', u'Ch', u'D', u'Đ',
                         u'E', u'Ê', u'G', u'Gh', u'Gi', u'H', u'I',
                         u'K', u'Kh', u'L', u'M', u'N', u'Ng', u'Ngh', u'Nh',
                         u'O', u'Ô', u'Ơ', u'P', u'Ph', u'Q', u'R',
                         u'S', u'T', u'Th', u'Tr', u'U', u'Ư', u'V',
                         u'X', u'Y', u'F', u'J', u'W', u'Z']

viet_consonants_lower = [u'a', u'ă', u'â', u'b', u'c', u'ch', u'd', u'đ',
                         u'e', u'ê', u'g', u'gh', u'gi', u'h', u'i',
                         u'k', u'kh', u'l', u'm', u'n', u'ng', u'ngh', u'nh',
                         u'o', u'ô', u'ơ', u'p', u'ph', u'q', u'r',
                         u's', u't', u'th', u'tr', u'u', u'ư', u'v',
                         u'x', u'y', u'f', u'j', u'w', u'z']

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
                'U7':u7[0], 'U71':o7[1], 'U72':o7[2], 'U73':o7[3], 'U74':o7[4],  'U75':o7[5],
                'u7':u7[6], 'u71':o7[7], 'u72':o7[8], 'u73':o7[9], 'u74':o7[10], 'u75':o7[11],
                'D9': u'Đ', 'd9': u'đ',
                'A1':a[1], 'A2':a[2], 'A3':a[3], 'A4':a[4],  'A5':a[5],
                'a1':a[7], 'a2':a[8], 'a3':a[9], 'a4':a[10], 'a5':a[11],
                'E1':e[1], 'E2':e[2], 'E3':e[3], 'E4':e[4],  'E5':e[5],
                'e1':e[7], 'e2':e[8], 'e3':e[9], 'e4':e[10], 'e5':e[11],
                'I1':i[1], 'I2':i[2], 'I3':i[3], 'I4':i[4],  'I5':i[5],
                'i1':i[7], 'i2':i[8], 'i3':i[9], 'i4':i[10], 'i5':i[11],
                'O1':i[1], 'O2':i[2], 'O3':i[3], 'O4':i[4],  'O5':i[5],
                'o1':i[7], 'o2':i[8], 'o3':i[9], 'o4':i[10], 'o5':i[11],
                'U1':i[1], 'U2':i[2], 'U3':i[3], 'U4':i[4],  'U5':i[5],
                'u1':i[7], 'u2':i[8], 'u3':i[9], 'u4':i[10], 'u5':i[11],
                }


telex_mappings = {'Aw':a8[0], 'Aws':a8[1], 'Awf':a8[2], 'Awr':a8[3], 'Awx':a8[4],  'Awj':a8[5],
                  'aw':a8[6], 'aws':a8[7], 'awf':a8[8], 'awr':a8[9], 'awx':a8[10], 'awj':a8[11],
                  'Aa':a6[0], 'Aas':a6[1], 'Aaf':a6[2], 'Aar':a6[3], 'Aax':a6[4],  'Aaj':a6[5],
                  'aa':a6[6], 'aas':a6[7], 'aaf':a6[8], 'aar':a6[9], 'aax':a6[10], 'aaj':a6[11],
                  'Ee':e6[0], 'Ees':e6[1], 'Eef':e6[2], 'Eer':e6[3], 'Eex':e6[4],  'Eej':e6[5],
                  'ee':e6[6], 'ees':e6[7], 'eef':e6[8], 'eer':e6[9], 'eex':e6[10], 'eej':e6[11],
                  'Oo':o6[0], 'Oos':o6[1], 'Oof':o6[2], 'Oor':o6[3], 'Oox':o6[4],  'Ooj':o6[5],
                  'oo':o6[6], 'oos':o6[7], 'oof':o6[8], 'oor':o6[9], 'oox':o6[10], 'ooj':o6[11],
                  'Ow':o7[0], 'Oos':o7[1], 'Oof':o7[2], 'Owr':o7[3], 'Owx':o7[4],  'Owj':o7[5],
                  'ow':o7[6], 'ows':o7[7], 'oof':o7[8], 'owr':o7[9], 'owx':o7[10], 'owj':o7[11],
                  'Uw':u7[0], 'Uws':o7[1], 'Uwf':o7[2], 'Uwr':o7[3], 'Uwx':o7[4],  'Uwj':o7[5],
                  'uw':u7[6], 'uws':o7[7], 'uwf':o7[8], 'uwr':o7[9], 'uwx':o7[10], 'uwj':o7[11],
                  'Dd': u'Đ', 'dd': u'đ',
                  'As':a[1], 'Af':a[2], 'Ar':a[3], 'Ax':a[4],  'Aj':a[5],
                  'as':a[7], 'af':a[8], 'ar':a[9], 'ax':a[10], 'aj':a[11],
                  'Es':e[1], 'Ef':e[2], 'Er':e[3], 'Ex':e[4],  'Ej':e[5],
                  'es':e[7], 'ef':e[8], 'er':e[9], 'ex':e[10], 'ej':e[11],
                  'Is':i[1], 'If':i[2], 'Ir':i[3], 'Ix':i[4],  'Ij':i[5],
                  'is':i[7], 'if':i[8], 'ir':i[9], 'ix':i[10], 'ij':i[11],
                  'Os':i[1], 'Of':i[2], 'Or':i[3], 'Ox':i[4],  'Oj':i[5],
                  'os':i[7], 'of':i[8], 'or':i[9], 'ox':i[10], 'oj':i[11],
                  'Us':i[1], 'Uf':i[2], 'Ur':i[3], 'Ux':i[4],  'Uj':i[5],
                  'us':i[7], 'uf':i[8], 'ur':i[9], 'ux':i[10], 'uj':i[11],

                }

def viet_ime(s, mapping='vni', raise_keyerror=False):
    if mapping == 'vni':
        _mapping = vni_mappings
        _pattern = r'[A-Za-z]\d+'
        if raise_keyerror:
            return re.sub(r'[A-Za-z]\d+',lambda m: _mapping[m.group(0)], s)
        else:
            return re.sub(r'[A-Za-z]\d+',lambda m: _mapping.get(m.group(0), m.group(0)),s)
    elif mapping == 'telex':
        _mapping = telex_mappings
        _pattern = '|'.join(re.escape(word) for word in
                            sorted(_mapping, key=len, reverse=True))
        return re.sub(_pattern, lambda match:telex_mappings[match.group()], s)


# Shield the top level imports from all the local variables.
__all__ = ['viet_vowels', 'viet_consonants', 'viet_utf8', 'viet_tones',
           'vni_mappings', 'telex_mappings', 'viet_ime']
