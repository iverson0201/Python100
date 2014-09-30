# -*- coding:utf-8 -*-
"""
描述：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
第10次落地时，共经过多少米？第10次反弹多高？
"""

def seq(times) :
	sequence=[]
	height=100
	for i in range(1,times+1) :
		sequence.append(height+height/2)
		height/=2
	return sequence

if __name__ == '__main__':
	value=seq(10)[9]
	reb=value/3
	print(value-reb,reb)