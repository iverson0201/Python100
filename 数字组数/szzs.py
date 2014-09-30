# -*- coding:utf-8 -*-
"""
描述：有1、2、3、4四个数字，能组成多少个互不相同且无重复数字的三位数？都是
多少？
"""

if __name__=="__main__" :
	for i in range(1,5) :
		for j in range(1,5) :
			for k in range(1,5) :
				if i!=j and i!=k and j!=k :
					print(i,j,k,sep='',end=',')