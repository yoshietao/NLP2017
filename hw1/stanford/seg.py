#!/usr/bin/env python3
#vim: set fileencoding:utf-8

from nltk.tokenize.stanford_segmenter import StanfordSegmenter

segmenter = StanfordSegmenter(path_to_slf4j ="./segmenter/slf4j-api.jar",
path_to_jar="./segmenter/stanford-segmenter-3.5.2.jar",
 path_to_sihan_corpora_dict="./segmenter/data",
 path_to_model="./segmenter/data/pku.gz",
 path_to_dict="./segmenter/data/dict-chris6.ser.gz")


out = open('out','w')

def tosimple(filename):
	f = open(filename,'r')
	count = 0
	for line in f:
		if count%4 == 1:
			#segment this part
			#print line
			#print unicode(line,"utf-8")
			#print line.encode('UTF-8')
			result = segmenter.segment(unicode(line,"utf-8"))
			out.write(result.encode('UTF-8'))
		else:
			out.write(line)
		count = count + 1

tosimple('../data/simple/aspect_review.txt')

