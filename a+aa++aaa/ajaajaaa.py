# -*- coding:utf-8 -*-
"""
描述：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222
(此时共有5个数相加)，几个数相加有键盘控制。
"""

def sum(n,c) :
	value=0
	tmp=0
	for i in range(0,c) :
		tmp=n*(10**i)+tmp
		value+=tmp
	return value

if __name__ == '__main__':
	print(sum(int(input("哪个数：")),int(input("几次："))))