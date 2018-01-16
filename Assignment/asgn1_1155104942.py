#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def problem_1(a, b):
    num = 0
    for x in range (a, b):
        if (x%7==0) and (x%3!=0):
            num=num+1
    return num
print (problem_1(10, 30))


def problem_2(n):
    result = 0
    a = n
    b = int("%s%s%s" %(n,n,n))
    c = int("%s%s%s%s%s" %(n,n,n,n,n))
    result = ("%d + %d + %d = %d" %(a, b, c, a+b+c))
    return result
print(problem_2(8))

