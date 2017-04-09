# -*- coding:utf-8 -*-
from scipy.stats import chi2_contingency as chi
import numpy as np


txt=['服务','态度','人员','环境','客房','设备','空调','价格','房价','交通','地理','餐厅','早餐']
txtcount = [27802,9701,8943,10376,2422,3004,6372,10142,1302,13315,18912,3827,23053]
total = 6025248

obs  = np.zeros((2,2))		#observation matrix

f = open('count_chi_no.txt','r')

for line in f:
	temp = line.split()
	for i in range(len(txt)):
		obs[0,0] = int(temp[i+2])
		obs[0,1] = int(temp[1])-obs[0,0]
		obs[1,0] = txtcount[i]-obs[0,0]
		obs[1,1] = total-obs[0,1]-obs[1,0]-obs[0,0]
		result = chi(obs,correction=False)
#		print result[0]
		if result[0] >= 500:
			print txt[i],temp[0],temp[15]


