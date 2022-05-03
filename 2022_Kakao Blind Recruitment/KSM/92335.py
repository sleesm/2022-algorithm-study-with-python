import math

def isPrime(num) :
    if num == 1 or num == 0 : return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True

def checkPrime(nums) :
    nums.reverse()
    sum = 0
    for i in range(0, len(nums)) :
        sum += nums[i] * pow(10,i)
    
    # print(sum)
    return isPrime(sum)

def solution(n, k):
    answer = 0
    num = []
    d = n
    
    while d > 0 :
        d,v = divmod(d,k)
        num.append(v)
        
    num.reverse()
    num.append(0)
    # print(num)
    
    j = 0
    for i in range(0, len(num)) :
        if num[i] == 0:
            # print(j, i, num[j:i])
            if checkPrime(num[j:i]) :
                answer +=1
                # print("stop")
            j = i
    
    # print(answer)
    return answer