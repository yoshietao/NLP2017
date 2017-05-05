# -*- coding:utf-8 -*-
from gensim.models import Word2Vec
import jieba.posseg as pseg
from operator import add
import numpy as np

f  = open('../data/polarity_review.txt','r')
fo = open('../data/aspect_review_po.txt','w')

c = Word2Vec.load('../data/model_pos_web')

aspect = ['服务','环境','价格','交通','餐厅']

for i,line in enumerate(f):
	fo.write(str(i)+'\n')
	x = line.split()
	fo.write(line)
	if x[0] == '-1':
		fo.write('\n')
	words = pseg.cut(line)
	for word,flag in words:
		try:
			for j in aspect:
				#print word,j
				#print c.similarity(word.encode('UTF-8'),j)
				if c.similarity(word.encode('UTF-8'),j)>0.6:
					fo.write(j+' ')
		except:
			True
	fo.write('\n')
	if x[0] == '1':
		fo.write('\n')
			
	
	
