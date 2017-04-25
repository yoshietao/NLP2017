# -*- coding:utf-8 -*-
import nltk
from gensim.models import Word2Vec

'''
text=[]
file=open('all_pos0.txt', 'r')
while True:
    line = file.readline()
    if not line: break
    text.append(line.split())
file.close()


c = Word2Vec(text)
c.save('model_pos_web')

'''

c  = Word2Vec.load('data/model_pos_web')
fo = open('data/aspects.txt','w')

num=20

txt=['服务','态度','人员','环境','客房','设备','空调','价格','房价','交通','地理','餐厅','早餐']
#	   1    1      1     2     2     2      2     3     3      4     4      5     5

dict1 = {}

for j in range(len(txt)):
	print txt[j]
	dict1[txt[j]] = True
	similar=c.most_similar(txt[j], topn=num)
	print txt[j]
	for i in range(num):
		print similar[i][0]
		if similar[i][0] not in dict1:
			dict1[similar[i][0]] = True
			fo.write(similar[i][0]+' ')
	print ' '
	print c.similarity(txt[j],similar[19][0])
	fo.write(str(c.similarity(txt[j],similar[19][0]))+'\n')
'''
for i in dict1:
	fo.write(i+'\t')
'''
	
	
