import math

def setTime(time):
    a = time.split(":")
    return int(a[0])*60+int(a[1])
    
def solution(fees, records):
    
    a = {}
    b = {}
    for i in records:
        str = i.split()
        
        if(str[1] not in a and str[2]=="IN"):
            a[str[1]] = setTime(str[0])
        elif(str[1] in a and str[2]=="OUT"):
            if(str[1] in b):
                b[str[1]] += setTime(str[0]) - a[str[1]]
            else :
                b[str[1]] = setTime(str[0]) - a[str[1]]
            del a[str[1]]
            
    for key in a:
        if(key in b):
            b[key] += setTime("23:59") - a[key]
        else :
            b[key] = setTime("23:59") - a[key]
    

    dct = dict((x, y) for x, y in sorted(b.items()))
    
    answer = []
    for key in dct:
        if(int(math.ceil(((dct[key]-fees[0])/fees[2])))>=0):
            answer.append(fees[1]+int(math.ceil(((dct[key]-fees[0])/fees[2])))*fees[3])
        else:
            answer.append(fees[1])
    
    
    return(answer)
