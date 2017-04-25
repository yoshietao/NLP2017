import jieba.posseg as pseg
import jieba

name='all.txt'
f  = open('../hw1_data/'+name,'r')
#f = open('test','r')
fo = open('all_pos.txt','w')

adj = {}

for i,line in enumerate(f):
	#if i%2 == 1:
	words = pseg.cut(line)
	for word, flag in words:
		fo.write(word.encode('UTF-8')+' ')

			#if flag in ['an']:
			#print word,flag
			#if flag in ['a']:#,'c','x', 'v', 's', 'vn', 'an', 'nr']:
				#adj[word] = True
	#fo.write('\n')

#for i in adj:
#	fo.write(i.encode('UTF-8')+' ')
