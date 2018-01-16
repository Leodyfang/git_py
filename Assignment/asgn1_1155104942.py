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

def problem_3(nums):
    max_sum = 0
    L = []
    LL = len(nums) - 2
    i = 0
    while i < LL
        L.append(sum(nums[i:i + 3]))
        ++i
    max_sum = max(L)
    return max_sum
nums  = [1, 3, -2, 4, 8, -9, 0, 5]
print(problem_3(nums))

def problem_04(sentence):
    ouput = ""
    words = sentence.split()
    output = ' '.join(sorted(words))
    return output
sentence = "chinese hong kong of the university"
print(problem_04(sentence))


def problem_05(sentence):
    output = []
    counts = dict()
    words = sentence.lower().split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    L = []
    for key,value in counts.items():
        L.append((value, key))
    output =  sorted(L,key = lambda x:x[0],reverse=True)
    output = output[0:5]
    return output

sentence = """
    The Transmission Control Protocol (TCP) is one of the main protocols of the Internet protocol suite. It originated in the initial network implementation in which it complemented the Internet Protocol (IP). Therefore, the entire suite is commonly referred to as TCP/IP. TCP provides reliable, ordered, and error-checked delivery of a stream of octets between applications running on hosts communicating by an IP network. Major Internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP. Applications that do not require reliable data stream service may use the User Datagram Protocol (UDP), which provides a connectionless datagram service that emphasizes reduced latency over reliability.
"""
print(problem_05(sentence))


