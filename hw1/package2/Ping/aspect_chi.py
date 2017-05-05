# -*- coding:utf-8 -*-
from scipy.stats import chi2_contingency as chi
from gensim.models import Word2Vec
from operator import add
import numpy as np

f  = open('../data/po+as_pos.txt','r')
f1 = open('../data/aspect_review_po.txt','r')

aspect = ['服务','环境','价格','交通','餐厅']

words = []
for line in f:
	words.append(line.split())

vocabulary = {}
for i in words:
	for j in i:
		vocabulary[j] = [0,0,0,0,0,0,0,0,0,0]
#print len(vocabulary)

for i,line in enumerate(f1):
	index = i/4
	if i%4 == 2 or i%4 == 3:
		pos_aspect = line.split()
		for j in pos_aspect:
			aspect_index = aspect.index(j)
			for k in words[index]:
				if i%4 == 2:
					vocabulary[k][aspect_index] = vocabulary[k][aspect_index]+1
				else:
					vocabulary[k][aspect_index+5] = vocabulary[k][aspect_index+5]+1
#print vocabulary

total = 0
total_asp = np.zeros(len(vocabulary))
total_w   = np.zeros(10)
for index,i in enumerate(vocabulary):
	total_asp[index] = sum(vocabulary[i])
	total = total + total_asp[index]
	total_w = map(add,total_w,vocabulary[i])
total_asp = [int(x) for x in total_asp]


#				|w[i]						|not w[i]									|total
#---------------------------------------------------------------------------------------------------
# asp[j]		|voca[i][j]					|total_w[j]-voca[i][j]						|total_w[j]
#---------------------------------------------------------------------------------------------------
# not asp[j]	|total_asp[i]-voca[i][j]	|total-total_w[j]-total_asp[i]+voca[i][j]	|/
#---------------------------------------------------------------------------------------------------
#total			|total_asp[i]				|/											|total

c=Word2Vec.load('../data/model_pos_web')
fo = open('opinion_extraction_po','w')
opinion = {}

obs = np.zeros((2,2))
for index,i in enumerate(vocabulary):
	if not (sum(vocabulary[i][:5])>0 and sum(vocabulary[i][5:])>0):
		for j in range(10):
			obs[0,0] = vocabulary[i][j]
			obs[0,1] = total_w[j]-vocabulary[i][j]
			obs[1,0] = total_asp[index]-vocabulary[i][j]
			obs[1,1] = total-total_w[j]-total_asp[index]+vocabulary[i][j]
			if obs[0,0]>0:
				result = chi(obs,correction=False)
				if result[0]>0.3 and result[0]<100:
					try:
						if sum(vocabulary[i][:5])>0 and c.similarity(aspect[j%5],i)>0.2:
							if i not in opinion:
								opinion[i] = ([result[0],j])
							else:
								if result[0]>opinion[i][0]:
									opinion[i] = [result[0],j]
							print aspect[j%5],i,'1',result[0]
						elif sum(vocabulary[i][5:])>0 and c.similarity(aspect[j%5],i)>0.2:
							if i not in opinion:
								opinion[i] = ([result[0],j])
							else:
								if result[0]>opinion[i][0]:
									opinion[i] = [result[0],j]
							print aspect[j%5],i,'-1',result[0]
					except:
						True

for i in opinion:
	fo.write(i+' '+str(opinion[i][1]%5)+' ')
	if opinion[i][1]>=5:
		fo.write('-1\n')
	else:
		fo.write('1\n')