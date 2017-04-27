# -*- coding:utf-8 -*-
import nltk
from gensim.models import Word2Vec
import numpy as np
import jieba.posseg as pseg
import jieba


f=open('../data/test_review.txt','r')
c=Word2Vec.load('../data/model_pos_web')

li=0

indexx=[]
txt=[]
for line in f:
	if(li%2!=0):
		txt.append(line)
	else:
		indexx.append(int(line))
	li=li+1

#print txt
#print indexx


			

words=[]
cuts=[]
for i in range(len(txt)):
	words=pseg.cut(txt[i])
	tmp=[]
	for word, flag in words:
		tmp.append(word)
	cuts.append(tmp)

print len(cuts)


tt=[]
fl=open('oplist','r')
for line in fl:
	tt.append(line.split())


pos=tt[0]
neg=tt[1]


aspect=[[u'服务',u'态度',u'人员'],[u'环境',u'客房',u'设备',u'空调'],[u'价格',u'房价'],[u'交通',u'地理'],[u'餐厅',u'早餐']]

matrix=np.zeros((len(cuts),5))

foo = open('history','w')

for yy in range(len(cuts)):
	foo.write(str(indexx[yy])+'\n')
	#print indexx[yy]
	#print '\n'
	txt=cuts[yy]
	#print txt
	flag=5
	for i in txt:
		try:
			i=i.encode('UTF-8')
			c[i] 
			
			if flag!=5:
				if (i in pos) and flag!=5:
					foo.write('  +1  '+str(i))
					#print '   +1  '+i
					matrix[yy][flag]=matrix[yy][flag]+1		
					#flag=5
				if (i in neg) and flag!=5:
					foo.write('  -1  '+str(i))
					#print '   -1  '+i
					matrix[yy][flag]=matrix[yy][flag]-1		
					#flag=5

			

			for ii in range(5):
				j=aspect[ii]
				for k in j:
					if c.similarity(k.encode('UTF-8'),i)>0.5:
						#print i
						foo.write('\n'+i+'\n')
						flag=ii
						
		except KeyError:
			1
	#print '\n\n'
	foo.write('\n\n')

#print matrix

test=np.zeros((1737,2))

cat=['服务','环境','价格','交通','餐厅']

ff=open('../data/test.csv','r')
li=1
for line in ff:
	if li!=0:
		ll=line.split(',')
		test[li-1][0]=indexx.index(int(ll[1]))
		cc=ll[2]
		ll[2]=cc[0:len(cc)-1]
		test[li-1][1]=cat.index(ll[2])
	li=li+1



fo=open('testing3_NTUSD_flag!=5_nopu.csv','w')

fo.write('id,Label\n')

for i in range(1737):
	fo.write(str(i+1))
	fo.write(',')

	ans=0;
	if matrix[int(test[i][0])][int(test[i][1])]>0:
		ans=1
	elif matrix[int(test[i][0])][int(test[i][1])]<0:
		ans=-1
	else:
		ans=0
	fo.write(str(int(ans)))
	fo.write('\n')






