#vim: set fileencoding:utf-8

from opencc import OpenCC 

openCC = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese
# can also set conversion by calling set_conversion
# openCC.set_conversion('s2tw')
to_convert = u'开放中文转换'
converted = openCC.convert(to_convert)