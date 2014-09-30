# -*- coding:utf-8 -*-

def level(score) :
	if score>=90 :
		return 'A'
	else :
		if score>=60 :
			return 'B'
		else :
			return 'C'

if __name__ == "__main__" :
	score=int(input("请输入分数："))
	print("Level:",level(score))
