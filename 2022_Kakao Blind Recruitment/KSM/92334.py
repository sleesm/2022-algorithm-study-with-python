# 2022 KAKAO BLIND RECRUITMENT 신고 결과 받기

# list.count(a) 는 list 안의 a 요소의 개수 구하는 방법

def solution(id_list, report, k):
    answer = []
    s1 = [s.split()[1] for s in set(report)]
    print(s1)
    s3 = [s2 for s2 in set(s1) if s1.count(s2) >= k]
    print(s3)
    s4 = [s.split()[0] for s in set(report) if s.split()[1] in s3]
    print(s4)
    answer = [s4.count(i) for i in id_list]
    return answer
