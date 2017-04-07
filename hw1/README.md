# NLP2017

#### 忽然想到 如果搜不到的字，或是同意詞沒擴充好，其實就等於是放進 0(neutral)而已，好像也不至於不能做XD
#### 需要斷詞的有：aspect_review, polarity_review, test_review
#### aspect_term.txt裡根本沒東西OAO 要自己建 。
***
    stanford+nltk toolkit:
    簡體較適合
    先segment->pos tagging or parse tree
***
#### opencc:
https://github.com/yichen0831/opencc-python
    
*** 
#### 詞性：
https://github.com/memect/kg-beijing/wiki/%E4%B8%AD%E6%96%87%E8%AF%8D%E6%80%A7%E6%A0%87%E8%AE%B0%E9%9B%86
#### 編碼：
http://blog.wahahajk.com/2009/08/unicodedecodeerror-ascii-codec-cant.html
http://www.prudentman.idv.tw/2015/08/python-string-list-chinese-encode-decode.html
#### kaggle:
https://kaggle.com/join/ntunlp2017project1
#### 關於編碼，如果從function出來的話，就會是unicode string,如果是直接宣告的話，ex: x = "chat",出來會是byte string的格式
#### 剛剛發現，如果讀取中文的file,讀進來會是byte string的格式，所以就都轉unicode string吧~
#### 不過由於這不是宣告，所以不能用 u"chat"來轉，所以：unicode(line,"utf-8") 可以用來轉line這個byte string variable
***
    方法一：
    word embedding, 
    N+adj --> 1 or -1 大量蒐集 --->train
    test,
