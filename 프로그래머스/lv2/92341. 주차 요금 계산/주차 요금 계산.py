import copy
import math

def time_to_minute(time):
    split_time = time.split(":")
    minute = int(split_time[0]) * 60 + int(split_time[1])
    return minute

def solution(fees, records):
    records = list(map(lambda x : x.split(), records))
    arr = [0]*time_to_minute('23:59')
    times = {}
    
    # 출입 기록
    for record in records:
        car_num = int(record[1])
        # 차가 처음 들어온 경우
        if car_num not in times:
            new_arr = copy.deepcopy(arr)
            new_arr[time_to_minute(record[0])] = 1
            times[car_num] = new_arr
        # 이전에 들어왔던 적이 있는 경우
        else : 
            if record[2] == 'IN':
                times[car_num][time_to_minute(record[0])] = 1
            else:
                times[car_num][time_to_minute(record[0])] = -1

    # Prefix_Sum
    for arr in times.values():
        for i in range(1, time_to_minute('23:59')):
            arr[i] += arr[i-1]
    for car_num, arr in times.items():
        times[car_num] = sum(arr)
    
    # 요금 계산
    for car_num, time in times.items():
        # 기본 시간 보다 작거나 같다면 -> 기본 요금
        if time <= fees[0]:
            times[car_num] = fees[1]
        # 기본 시간 보다 오래 이용 -> 초과 요금
        else:
            times[car_num] = fees[1] + math.ceil((time-fees[0])/fees[2])*fees[-1]
            
    answer = list(map(lambda x : x[1], sorted(times.items())))
    
    return answer