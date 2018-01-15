def problem_1(a, b):
    num = 0
    for x in range (a, b):
        if (x%7==0) and (x%3!=0):
            num=num+1
    return num
print (problem_1(10, 30))