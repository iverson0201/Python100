# -*- coding:utf-8 -*-
"""
描述：判断101-200之间有多少个素数，并输出所有素数。s
标签：判断素数
"""
import math

def isPrime(num) :
	for i in range(2,math.ceil(math.sqrt(num))) :
		if num%i == 0 :
			return False
	return True

if __name__ == "__main__" :
	result=[]
	for i in range(101,201) :
		if isPrime(i) :
			result.append(i)
	print(result)