# -*- coding:utf-8 -*-
import jieba.posseg as pseg
import jieba

name='test_review.txt'
f  = open('../data/simple/'+name,'r')
fo = open('../pos_test.txt','w')

#i = 0
for line in f:
	#if i%4 == 1:
		words = pseg.cut(line)
		for word, flag in words:
			if flag in ['l']:
				print word,flag
			#if flag in ['n','a', 'v', 's', 'vn', 'an', 'nr']:
			#	string=word+' '
			#	fo.write(string.encode('utf8'))
		#fo.write('\n')
	#i = i + 1