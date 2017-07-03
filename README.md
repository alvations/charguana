Charguana
====

A library for *"character vommitting"*.

Only works in `Python3`


Install
====

```bash
pip3 install charguana
```


Usage
====

**CJK characters**:

```python
>>> from charguana import get_charset

# Hiragana.
>>> ''.join(list(get_charset('hiragana')))
'\u3040ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ\u3097\u3098゙゚゛゜ゝゞゟ'

# Katakana.
>>> ''.join(list(get_charset('katakana')))
'゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿ'

# Bopomofo.
>>> ''.join(list(get_charset('bopomofo')))
'\u3100\u3101\u3102\u3103\u3104ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩㄪㄫㄬㄭ\u312e\u312f'

# Punctuations
>>> ''.join(list(get_charset('punctuation')))
'\u3000、。〃〄々〆〇〈〉《》「」『』【】〒〓〔〕〖〗〘〙〚〛〜〝〞〟〠〡〢〣〤〥〦〧〨〩〪〭〮〯〫〬〰〱〲〳〴〵〶〷〸〹〺〻〼〽〾〿'

# Romanji
>>> ''.join(list(get_charset('romanji')))
'\uff00！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～｟｠｡｢｣､･ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝﾞﾟﾠﾡﾢﾣﾤﾥﾦﾧﾨﾩﾪﾫﾬﾭﾮﾯﾰﾱﾲﾳﾴﾵﾶﾷﾸﾹﾺﾻﾼﾽﾾ\uffbf\uffc0\uffc1ￂￃￄￅￆￇ\uffc8\uffc9ￊￋￌￍￎￏ\uffd0\uffd1ￒￓￔￕￖￗ\uffd8\uffd9ￚￛￜ\uffdd\uffde\uffdf￠￡￢￣￤￥￦\uffe7￨￩￪￫￬￭￮\uffef'


# Chinese.
>>> from charguana import tradify, simplify
>>> ''.join(list(get_charset('chinese'))) == ''.join(list(get_charset('zh')))
True
>>> ''.join(list(get_charset('zh'))) == ''.join(list(get_charset('cn')))
True
>>> list(get_charset('simplified_chinese'))[:10]
['锕', '皑', '蔼', '碍', '爱', '嗳', '嫒', '瑷', '暧', '霭']
>>> list(get_charset('traditional_chinese'))[:10]
['錒', '皚', '藹', '礙', '愛', '噯', '嬡', '璦', '曖', '靄']
>>> simplify('錒')
'锕'
>>> tradify('锕')
'錒'

# Japanese.
>>> ''.join(list(get_charset('japanese'))) == ''.join(list(get_charset('ja')))
True
>>> ''.join(list(get_charset('ja'))) == ''.join(list(get_charset('jp')))
True

# Korean.
>>> ''.join(list(get_charset('korean'))) == ''.join(list(get_charset('ko'))) == ''.join(list(get_charset('kr')))
True
>>> ''.join(list(get_charset('ko'))) == ''.join(list(get_charset('kr')))
True

# All Chinese, Korean, Japanese and Romanji.
>>> ''.join(list(get_charset('cjk')))
```


**Perluniprops Characters**:


```python
>>> from charguana import get_charset

# Open Punctuation.
>>> ''.join(get_charset('Open_Punctuation'))
'([{༺༼᚛‚„⁅⁽₍〈❨❪❬❮❰❲❴⟅⟦⟨⟪⟬⟮⦃⦅⦇⦉⦋⦍⦏⦑⦓⦕⦗⧘⧚⧼⸢⸤⸦⸨〈《「『【〔〖〘〚〝﴾︗︵︷︹︻︽︿﹁﹃﹇﹙﹛﹝（［｛｟｢'

# Close Punctuation.
>>> ''.join(get_charset('Close_Punctuation'))
')]}༻༽᚜⁆⁾₎〉❩❫❭❯❱❳❵⟆⟧⟩⟫⟭⟯⦄⦆⦈⦊⦌⦎⦐⦒⦔⦖⦘⧙⧛⧽⸣⸥⸧⸩〉》」』】〕〗〙〛〞〟﴿︘︶︸︺︼︾﹀﹂﹄﹈﹚﹜﹞）］｝｠｣'

# Currency Symbols.
>>> ''.join(get_charset('Currency_Symbol'))
'$¢£¤¥֏؋৲৳৻૱௹฿៛₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺꠸﷼﹩＄￠￡￥￦'

# Numbers.
>>> ''.join(list(get_charset('IsN'))[:50])
'0123456789²³¹¼½¾٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹߀߁߂߃߄߅߆߇߈߉०१२३'

# Alphabetic
>>> ''.join(list(get_charset('IsAlpha'))[:50])
'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx'

# Lowercase.
>>> ''.join(list(get_charset('IsLower'))[:50])
'abcdefghijklmnopqrstuvwxyzªµºßàáâãäåæçèéêëìíîïðñòó'

# Uppercase.

>>> ''.join(list(get_charset('IsUpper'))[:50])
'ABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØ'
# Alphanumeric
>>> ''.join(list(get_charset('IsAlnum'))[:50])
'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn'
```

**Thai**

```python
# Thai.
>>> ''.join(list(get_charset('thai')))[:50]
'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ\u0e7f฿ะั'
# Thai consonants.
>>> from charguana import get_charset_ranges
>>> from charguana.thai import thai_consonants
>>> list(get_charset_ranges([thai_consonants]))[:10]
['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช']
# Thai Vowels
>>> from charguana.thai import thai_vowels_1, thai_vowels_2
>>> list(get_charset_ranges([thai_vowels_1, thai_vowels_2]))[:10]
['ะ', 'ั', 'า', 'ำ', 'ิ', 'ี', 'ึ', 'ื', 'ุ', 'ู']
```

**Vietnamese**

```python
# Vietnamese
>>> from charguana import get_charset
>>> ''.join(list(get_charset('viet'))[:50])
'AĂÂBCChDĐEÊGGhGiHIKKhLMNNgNghNhOÔƠPPhQRSTThTrUƯVXYFJWZaăâbcchd'

>>> from charguana import get_charset
>>> ''.join(list(get_charset('viet'))[:50])
'AĂÂBCChDĐEÊGGhGiHIKKhLMNNgNghNhOÔƠPPhQRSTThTrUƯVXYFJWZaăâbcchd'

# Vietnamese tones.
>>> from charguana.viet import viet_tones
>>> viet_tones.huyen
'̀'
>>> 'o' + viet_tones.huyen
'ò'
>>> 'o' + viet_tones.sac
'ó'
>>> 'o' + viet_tones.hoi
'ỏ'
>>> 'o' + viet_tones.nga
'õ'
>>> 'o' + viet_tones.nang
'ọ'
>>> 'o' + viet_tones.ngang
'o'

# Vietnamese consonants.
>>> from charguana.viet import viet_consonants
>>> list(viet_consonants)
['A', 'Ă', 'Â', 'B', 'C', 'Ch', 'D', 'Đ', 'E', 'Ê', 'G', 'Gh', 'Gi', 'H', 'I', 'K', 'Kh', 'L', 'M', 'N', 'Ng', 'Ngh', 'Nh', 'O', 'Ô', 'Ơ', 'P', 'Ph', 'Q', 'R', 'S', 'T', 'Th', 'Tr', 'U', 'Ư', 'V', 'X', 'Y', 'F', 'J', 'W', 'Z', 'a', 'ă', 'â', 'b', 'c', 'ch', 'd', 'đ', 'e', 'ê', 'g', 'gh', 'gi', 'h', 'i', 'k', 'kh', 'l', 'm', 'n', 'ng', 'ngh', 'nh', 'o', 'ô', 'ơ', 'p', 'ph', 'q', 'r', 's', 't', 'th', 'tr', 'u', 'ư', 'v', 'x', 'y', 'f', 'j', 'w', 'z']

# Vietnamese vowels with diacritics.
>>> from charguana.viet import a, a6, a8
>>> a
['A', 'Á', 'À', 'Ả', 'Ã', 'Ạ', 'a', 'á', 'à', 'ả', 'ã', 'ạ']
>>> a6
['Â', 'Ấ', 'Ầ', 'Ẩ', 'Ẫ', 'Ậ', 'â', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ']
>>> a8
['Ă', 'Ắ', 'Ằ', 'Ẳ', 'Ẵ', 'Ặ', 'ă', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ']

# Vietnamese tones.
>>> from charguana.viet import viet_tones
>>> viet_tones
Tones(ngang='', huyen='̀', sac='́', hoi='̉', nga='̃', nang='̣')
>>> 'o' + viet_tones.sac
'ó'
>>> 'o' + viet_tones.nang
'ọ'

# Vietnamese IME.
>>> from charguana.viet import viet_ime
>>> viet_ime('Nguye64n Tra62n Anh Thu7')
'Nguyễn Trần Anh Thư'
# IME typo.
>>> viet_ime('Nguye64n Tra62n Anh Thu8') # uncheck.
'Nguyễn Trần Anh Thu8'
>>> viet_ime('Nguye64n Tra62n Anh Thu8', raise_keyerror=True) # check.
...
KeyError: 'u8'
# Telex
>>> viet_ime('Nguyeefn Traafn Anh Thuw', mapping='telex')
'Nguyền Trần Anh Thư'
# Short cut for TELEX ime with functools.partial
>>> from functools import partial
>>> from charguana.viet import viet_ime
>>> telex_ime = partial(viet_ime, mapping='telex')
>>> telex_ime('Nguyeefn Traafn Anh Thuw')
'Nguyền Trần Anh Thư'
```
