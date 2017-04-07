# encoding=utf-8
import numpy as np
import jieba

def openfile(filename):
	f = open(filename,'r')
	count = 0
	for line in f:
		if count%4 == 1:
			#segment this part
			seg_list = jieba.cut(line, cut_all=True)
			print ("Full Mode: " + "/ ".join(seg_list))
		count = count + 1


#seg_list = jieba.cut("该是来音乐会展现气质的时候了", cut_all=True)

#print("Full Mode: " + "/ ".join(seg_list))

x = openfile('data/aspect_review.txt')