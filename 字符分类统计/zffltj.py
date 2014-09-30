# -*-coding:utf-8 -*-

"""
描述：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
标签：字符分类统计
"""

def count(str) :
	counter={"char":0,"digit":0,"space":0,"others":0}
	for i in str :
		index=ord(i)
		if  65<=index<=90 or  97<=index<=122 :
			counter["char"]=counter["char"]+1
		elif 48<=index<=57:
			counter["digit"]=counter["digit"]+1
		elif index==32 or index==9 :
			counter["space"]=counter["space"]+1
		else :
			counter["others"]=counter["others"]+1
	return counter


if __name__ == "__main__" :
	string=input("请输入一个字符串：")
	for k,v in count(string).items() :
		print(k,'：',v)