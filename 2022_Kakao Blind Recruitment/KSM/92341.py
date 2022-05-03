import math


def setTime(time):
    hour, min = map(int, time.split(":"))
    return hour * 60 + min


def calculateFees(fees, times):
    min = (times - fees[0])
    if min > 0:
        return fees[1] + math.ceil((min/fees[2])) * fees[3]
    return fees[1]


def solution(fees, records):
    answer = []
    cars = {}  # 누적 주차 시간 저장
    tmpCars = {}  # 이전 주차 시간 저장
    InCars = []  # 출차 내역 없는 차 번호 저장
    records = list(map(lambda x: x.split(), records))
    for record in records:
        carNum = record[1]

        if record[2] == "IN":
            InCars.append(carNum)
            if carNum not in cars:
                cars[carNum] = setTime(record[0])
            else:
                tmpCars[carNum] = cars[carNum]
                cars[carNum] = setTime(record[0])
                # print("이전 주차 시간", carNum, tmpCars[carNum])

        elif record[2] == "OUT":
            InCars.remove(carNum)
            tmp = cars[carNum]  # 출입 시간
            # print("tmpCars", tmpCars , record[0])
            if carNum in tmpCars:  # 이전 주차 시간이 있을 경우
                # print("이전 주차 시간 있음" , carNum, tmpCars[carNum])
                cars[carNum] = (tmpCars[carNum] + (setTime(record[0]) - tmp))
                # print(cars[carNum])
            else:
                cars[carNum] = (setTime(record[0]) - tmp)

    # print("InCars" , InCars)

    for x in InCars:
        tmp = cars[x]
        if x in tmpCars:
            # print("이전 주차 시간 있음" , x, tmpCars[x])
            cars[x] = (tmpCars[x] + (setTime("23:59") - tmp))
            # print(cars[x])
        else:
            cars[x] = (setTime("23:59") - tmp)

    # print("cars", cars)
    cars = dict(sorted(cars.items()))
    # print("cars", cars)

    for x in cars:
        answer.append(calculateFees(fees, cars.get(x)))

    return answer
