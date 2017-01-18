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

```python
>>> ''.join(list(get_charset('hiragana')))
'\u3040ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ\u3097\u3098゙゚゛゜ゝゞゟ'
>>> ''.join(list(get_charset('katakana')))
'゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿ
>>> ''.join(list(get_charset('bopomofo')))
'\u3100\u3101\u3102\u3103\u3104ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩㄪㄫㄬㄭ\u312e\u312f'

>>> ''.join(list(get_charset('chinese'))) == ''.join(list(get_charset('zh'))) == ''.join(list(get_charset('cn')))
True
>>> ''.join(list(get_charset('japanese'))) == ''.join(list(get_charset('ja'))) == ''.join(list(get_charset('jp')))
True
>>> ''.join(list(get_charset('korean'))) == ''.join(list(get_charset('ko'))) == ''.join(list(get_charset('kr')))
True

>>> ''.join(list(get_charset('cjk')))
```
