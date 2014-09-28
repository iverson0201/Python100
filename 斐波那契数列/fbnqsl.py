# -*- coding:utf-8 -*- 
"""
描述：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后
每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
标签：斐波那契数列
"""

def Fibonacci(n) :
	rabbits=[1,1]
	for i in range(2,n+1) :
		rabbits.append(rabbits[i-2]+rabbits[i-1])
	return rabbits

if __name__ == "__main__" :
	print(Fibonacci(37))