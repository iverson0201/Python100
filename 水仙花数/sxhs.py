# -*- coding:utf-8 -*-
"""
描述：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和
等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三
次方。
标签：水仙花数
"""

def judge(num) :
    rel=0
    tmp=num
    while tmp>0 :
        rel+=(tmp%10)**3
        tmp//=10
    if rel==num :
        return True
    else :
        return False

if __name__ == "__main__" :
    for i in range(100,1000) :
        if judge(i) : 
            print(i,end=',')
