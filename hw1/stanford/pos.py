#vim: set fileencoding:utf-8
from nltk.tag import StanfordPOSTagger

chi_tagger = StanfordPOSTagger('./postagger/chinese-distsim.tagger',
path_to_jar='./postagger/stanford-postagger-3.7.0.jar')


#sent = u"入 住 退房 慢 , 电梯 慢 , 超市 破 , 房间 旧 , 服务 态度 差 !"
#for _, word_and_tag in  chi_tagger.tag(sent.split()):
#    word, tag = word_and_tag.split('#')
#    print word.encode('utf-8'), tag


out = open('../polarity_no_1.txt','w')

def pos(filename):
	f = open(filename,'r')
	c = 0
	for line in f:
		if c >= 0 and c<5000:
			x = []
			if c%500 == 0:
				print c/500
			x = unicode(line,"utf-8").split()
			if(x[0] == '1'):
				out.write('1\t')
			else:
				out.write('-1\t')
			for _, word_and_tag in  chi_tagger.tag(x):
			   	word, tag = word_and_tag.split('#')
				if tag not in  ['PU','DEC','LC','CD','AD','M','DT','AS','P','DEG'] :
					#print word
					out.write(word.encode('utf-8')+'\t')
			out.write('\n')
		c = c+1

pos('../polarity.txt')
