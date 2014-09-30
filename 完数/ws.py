# -*- coding:utf-8 -*-
"""
描述：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
找出1000以内的所有完数。
标签：完数
"""

def isCom(num) :
	sum=0
	for i in range(1,num) :
		if num%i==0 :
			sum+=i
		if sum>num :
			return False
	if sum==num :
		return True
	else :
		return False

if __name__ == '__main__':
	for i in range(1,1001) :
		if isCom(i) :
			print(i,end=' ')
