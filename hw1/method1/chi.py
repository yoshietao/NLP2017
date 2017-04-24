# -*- coding:utf-8 -*-
from scipy.stats import chi2_contingency as chi
from gensim.models import Word2Vec
from sklearn import ensemble
#from sklearn import tree
import numpy as np

# Aspect = {服務, 環境, 價格, 交通, 餐廳}

print "---------------define function--------------------------"
def simpleread(name):
	x = []
	f = open(name,'r')
	for line in f:
		x.append(line.split())
	return x

def compare(int1):
	if int1>0:
		return 1
	elif int1<0:
		return -1
	else:
		return 0

print '-----------------global read----------------------------'
f2  = open('new_aspects_class.txt','r')

aspect_class = []
for line in f2:
	aspect_class.append(line.split())
aspect_class_ = {}
for i in range(len(aspect_class)):
	aspect_class_[aspect_class[i][0]] = aspect_class[i][1]
print '----------reading aspects class complete----------------'
'''
print '----------------find train set--------------------------'
total = 0

obs  = np.zeros((2,2))		#observation matrix

fo  = open('aspect_opinion_label.txt','w')
fo1 = open('opinion_only.txt','w')
foo = open('train_data.txt','w')

c  = Word2Vec.load('model_posed_review')

count = simpleread('count_chi_no.txt')
count = np.array(count)
print 'count.shape =',count.shape


aspects = simpleread('new_aspects.txt')
aspects = aspects[0]

dict1 = {}
for i in range(count.shape[0]):
	dict1[count[i][0]] = count[i][1]
	total = total + int(count[i][1])
print "total",total

aspect_count = np.zeros(len(aspects))


for i in range(len(aspects)):
	if (aspects[i] in dict1):
		aspect_count[i] = dict1[aspects[i]]

opinion_only_ = {}

print '-------------chi square to every bi-gram in polarity review--------------------'

for j in range(count.shape[0]):
	for i in range(len(aspects)):
		temp = []
		if aspect_count[i] != 0:
			obs[0,0] = int(count[j][i+2])
			obs[0,1] = int(count[j][1])-obs[0,0]
			obs[1,0] = aspect_count[i]-obs[0,0]
			obs[1,1] = total-obs[0,1]-obs[1,0]-obs[0,0]
			result = chi(obs,correction=False)
			#print result[0]
			
			if result[0] >= 600:
				classs = int(aspect_class_[aspects[i]])-1 				#check to which aspect the opinion belongs
				if count[j][0] not in opinion_only_:
					opinion_only_[count[j][0]] = [0,0,0,0,0]	
				#print opinion_only_[count[j][0]]
				opinion_only_ [count[j][0]][classs] = opinion_only_ [count[j][0]][classs] + int(count[j][count.shape[1]-1])
			
				fo.write(aspects[i]+'\t'+count[j][0]+'\t'+count[j][count.shape[1]-1]+'\t'+'chi:'+str(result[0])+'\n')
				
				temp.extend(c[aspects[i]])
				temp.extend(c[count[j][0]])
				temp.append(count[j][count.shape[1]-1])
				for item in temp:
					foo.write("%s " % item)
				foo.write('\n')
				
for i in opinion_only_:
	if abs(np.sum(opinion_only_[i]))>=5:
		print i,opinion_only_[i]
		fo1.write(i+' ')
		for j in range(5):
			if opinion_only_[i][j] >0:
				fo1.write(str(1)+' ')
			elif opinion_only_[i][j] <0:
				fo1.write(str(-1)+' ')
			else:
				fo1.write(str(0)+' ')
		fo1.write('\n')

'''
print "---------------------------train-----------------------------"

f = open('train_data.txt','r')

X = []
Y = []
for line in f:
	ttemp = []
	temp = line.split()
	for x in temp[:len(temp)-1]:
		ttemp.append(float(x))
	X.append(ttemp)
	Y.append(int(temp[len(temp)-1]))
f.close()
#print X,Y
X = np.array(X)
Y = np.array(Y)
clf = ensemble.RandomForestClassifier()
#clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

print clf.score(X,Y)

print "---------------------------test------------------------------"

f  = open('test_data_delete_duplicate.txt','r')
fo = open('w2v_rf_degenerate.csv','w')
ff = open('test_proba','w')
fo.write('Id,Label\n')

c  = Word2Vec.load('model_posed_review')

test_index  = simpleread('test.csv')
degenerate_ = simpleread('degenerate_prediction.txt')

i = 1
for line in f:
	#print line
	score = np.zeros(5)
	normalize_factor = np.zeros(5)
	j = (i-1)*3
	if line == '\n':
		ff.write(str(i)+',0\n')
		while j < i*3:
			target = int(aspect_class_[test_index[j][2]])-1
			predict_value = compare(int(degenerate_[i-1][target]))
			fo.write(str(j+1)+','+str(predict_value)+'\n')
			j = j+1
	else:
		line = line.split()
		count = 0
		while count < len(line):
			test = c[line[count]].tolist()
			#print test
			if line[count+1] in c:
				test.extend(c[line[count+1]].tolist())
				test = np.array([test])
				#print test.shape
				#print clf.predict_proba(test)
				#print clf.predict(test)
				#if clf.predict_proba(test)[0][0]*clf.predict_proba(test)[0][1] <= 0.16:
				ff.write(str(i)+','+str(clf.predict_proba(test)[0])+',')
				if clf.predict_proba(test)[0][0] != 0.5:
					score[int(aspect_class_[line[count]])-1] = score[int(aspect_class_[line[count]])-1] + clf.predict(test)[0]
			count = count + 2
		#print score
		ff.write(str(score)+'\n')
		while j < i*3:
			value = compare(score[int(aspect_class_[test_index[j][2]])-1])
			#if value != 0:
			fo.write(str(j+1)+','+str(value)+'\n')
			#else:
			#	target = int(aspect_class_[test_index[j][2]])-1
			#	predict_value = compare(int(degenerate_[i-1][target]))
				#print target,degenerate_[i-1][target],predict_value
			#	fo.write(str(j+1)+','+str(predict_value)+'\n')
			j = j+1	
	i = i+1

#'''
