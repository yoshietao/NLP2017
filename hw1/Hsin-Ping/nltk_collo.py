# -*- coding:utf-8 -*-

from gensim.models import Word2Vec
import jieba.posseg as pseg
import nltk.collocations
import nltk.corpus
import collections

#f=open('data_cutt','r')
f = open('../data/all_pos.txt','r')
words=f.read().split()
#print words

#c=Word2Vec.load('data_cut_model')
c=Word2Vec.load('../data/model_pos_web')

#print c.similarity('方便','好')
#print c.similarity('高','好')

bgm    = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(words,window_size=3)
finder.apply_freq_filter(50)

scored = finder.score_ngrams( bgm.likelihood_ratio )


txt=['服务','态度','人员','环境','客房','设备','空调','价格','房价','交通','地理','餐厅','早餐']


oplist=[]
counter=0
for i in range(len(scored)):
	try:
		w1=scored[i][0][0]
		w2=scored[i][0][1]
		c[w1]
		c[w2]

		b1=0
		b2=0

		th=0.5

		for asp in txt:
			if c.similarity(w1,asp)>th:
				b1=1
			if c.similarity(w2,asp)>th:
				b2=1
		
		if not (b1==1 and b2==1):
			if (b1==1) :
				if(c.similarity(w2,'好')>0.1 or c.similarity(w2,'差')>0.1 ):
		#		print scored[i][0][0]+' '+scored[i][0][1]+'\n'
					if(w2 not in oplist):
						oplist.append(w2)
					counter=counter+1
			if (b2==1):
				if(c.similarity(w1,'好')>0.1 or c.similarity(w1,'差')>0.1 ):
	#			print scored[i][0][1]+' '+scored[i][0][0]+'\n'
					if(w1 not in oplist):
						oplist.append(w1)
					counter=counter+1
	except KeyError:
		1
		#print 'there is no '+scored[i][0][0]

print len(scored)
print counter

for i in range(len(oplist)):
	print str(i)+' '+oplist[i]
"""
# Group bigrams by first word in bigram.                                        
prefix_keys = collections.defaultdict(list)
for key, scores in scored:
   prefix_keys[key[0]].append((key[1], scores))

# Sort keyed bigrams by strongest association.                                  
for key in prefix_keys:
   prefix_keys[key].sort(key = lambda x: -x[1])



for word in txt:
	for i in range(5):
		print word,prefix_keys[word][i][0]
	print '\n'
"""
oplist.remove('有')
oplist.remove('是')
oplist.remove('很')

from sklearn import cluster
opvec=[]
for i in range(len(oplist)):
	opvec.append(c[oplist[i]])
	

k = 2
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(opvec)

print kmeans.labels_
print kmeans.cluster_centers_


pos=[]
neg=[]

for i in range(len(opvec)):
	if kmeans.labels_[i]==0:
		words = pseg.cut(oplist[i])
		for word, flag in words:
			if flag not in  ['x','c','m','r','y','p','t','uz','zg','uj','q','c','ug','ul']:
				print word,flag
				pos.append(oplist[i])
	else:
		words = pseg.cut(oplist[i])
		for word, flag in words:
			if flag not in  ['x','c','m','r','y','p','t','uz','zg','uj','q','c','ug','ul']:
				print word,flag
				neg.append(oplist[i])


if c.similarity(pos[0],'好')<0.35:
	temp = pos
	pos = neg
	neg = temp

f1 = open('../pos','r')
poss = f1.readline().split()
f2 = open('../neg','r')
negg = f2.readline().split()

f=open('oplist','w')
f.write(' '.join(pos+poss))
f.write('\n')
f.write(' '.join(neg+negg))

