# -*- coding:utf-8 -*-
from gensim.models import Word2Vec
import numpy as np
import nltk

f  = open('data/all_adj.txt','r')
f1 = open('data/aspects.txt','r')
fo = open('aspect_opinion_nolabel','w')

c  = Word2Vec.load('data/model_pos_web')


#print c.similarity('凶狠','呆滞'),c.similarity('粗鲁','凶狠')

opinion = []
for line in f:
	opinion = line.split()


aspect = []

for line in f1:
	aspect = line.split()
	threshold = aspect[len(aspect)-1]
	print threshold		
	for i in aspect[:len(aspect)-1]:
		for j in opinion:
			if j in c:
				if c.similarity(i,j) > 0.4:
					#print i,j,c.similarity(i,j)
					fo.write(i+' '+j+'\n')

