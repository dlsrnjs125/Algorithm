test_case = int(input())

for _ in range(test_case): # index를 무시하고 싶을 때 _사용
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)] # list의 index를 같이 저장하기 위해서
    count = 0
    
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]: # queue에 속해있는 요소들 중 가장 큰 가중치와 가장 앞의 인자의 가중치를 비교
            count += 1
            
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0) # 가장 큰 가중치는 맞지만 내가 원하는 index가 아님
        else:
            queue.append(queue.pop(0))
 # 수정