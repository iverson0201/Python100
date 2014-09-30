# -*- coding:utf-8 -*-
"""
描述：输入两个正整数m和n，求其最大公约数和最小公倍数。
标签：最大公约数，最小公倍数
"""

def cal(m,n) :
	if m>n :
		tmp=m
		m=n
		n=tmp
	tmp1=m
	tmp2=n
	while m!=0 :
		v=n%m
		n=m
		rel=m
		m=v
	return rel,tmp1*tmp2//rel

if __name__ == '__main__':
	num1=int(input("请输入第一个数："))
	num2=int(input("请输入第二个数："))
	print("最大公约数：{0}，最小公倍数：{1}".format(*cal(num1,num2)))