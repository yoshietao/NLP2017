# NLP2017

#### 忽然想到 如果搜不到的字，或是同意詞沒擴充好，其實就等於是放進 0(neutral)而已，好像也不至於不能做XD
#### 目前使用jieba斷詞系統，那，需要斷詞的有：aspect_review, polarity_review, test_review
#### aspect_term.txt裡根本沒東西OAO 要自己建 。
***
    stanford+nltk toolkit:
    簡體較適合
    先segment->pos tagging or parse tree
***
    opencc:
    https://github.com/yichen0831/opencc-python
***
    詞性：
    https://github.com/memect/kg-beijing/wiki/%E4%B8%AD%E6%96%87%E8%AF%8D%E6%80%A7%E6%A0%87%E8%AE%B0%E9%9B%86
    編碼：
    http://blog.wahahajk.com/2009/08/unicodedecodeerror-ascii-codec-cant.html
    http://www.prudentman.idv.tw/2015/08/python-string-list-chinese-encode-decode.html
