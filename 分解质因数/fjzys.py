# -*- coding:utf-8 -*-
"""
描述：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。 
标签：分解质因数
"""

def decompose(n) :
	rel=[]
	for i in range(2,n+1) :
		while n!=i :
			if n%i==0 :
				# 使用join必须保证列表里的元素是字符串类型的
				rel.append(str(i))
				n//=i
			else :
				break
	rel.append(str(n))
	print('*'.join(rel))


if __name__ == "__main__" :
	# 留意转型函数，而非 (int)
	num=int(input("请输入一个数："))
	decompose(num)


