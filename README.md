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
>>> ''.join(list(get_charset('chinese'))) == ''.join(list(get_charset('zh')))
True
>>> ''.join(list(get_charset('zh'))) == ''.join(list(get_charset('cn')))
True

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
