def problem_1(a,b):
    num = 0
    for i in range(a,b+1):
        if not (i%7) and (i%3):
            num += 1
    return num

def problem_2(n):
    result = 0
    if n in range(0,10):
        result = n + n*111 + n*11111
    return result

def problem_3(nums):
    max_sum = 0
    for i in range(len(nums)-2):
        sum = nums[i] + nums[i+1] + nums[i+2]
        if sum > max_sum:
            max_sum = sum
    return max_sum

def problem_4(sentence):
    output = " ".join(sorted(sentence.split()))
    return output

def problem_5(sentence):
    dic = {}
    for word in sentence.lower().split():
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    result = sorted(dic.items(), key=lambda x:x[1],reverse=True)[:5]
    output = [(y,x) for (x,y) in result]
    return output

def problem_6(path_to_file):
    output = []
    with open(path_to_file,"r") as f:
        lines = f.readlines()
    keys = lines[0].strip().split(",")
    for record in lines[1:]:
        values = record.strip().split(",")
        output.append(dict(zip(keys,values)))
    return output

if __name__ == "__main__":
    pass
    # print(problem_1(35,112))
    # print(problem_2(3))
    # print(problem_3([1,3,-2,4,8,-9,0,5]))
    # print(problem_4("This course can help you learn much"))
    # print (problem_5("The Internet Protocol (IP) is the principal network communications protocol in the Internet protocol suite for relaying datagrams across network boundaries and its routing function enables internetworking and essentially establishes the Internet"))
    # print(problem_6("test.csv"))
    # print(problem_6("test.csv"))