# 1. 배달할 물건이나, 회수할 물건이 i번째 까지 존재한다면, 반드시 i번째 까지는 적어도 한 번은 가야한다.
# 2. 한 번 출발하여, 물류창고로 돌아오면, cap만큼의 배달을 수행할 수 있고, cap만큼의 물건을 회수 해 올 수 있다.
# 3. 한 곳에서 택배를 전부 배달하지 못했거나, 회수하지 못했다면, 물류창고로 돌아왔다가, 다시 같은 장소로 떠나야 한다.
def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0

    for i in range(n-1, -1, -1):
        cnt = 0
        d -= deliveries[i]
        p -= pickups[i]
        while d < 0 or p < 0:
            d += cap
            p += cap
            cnt += 1
            
        answer += (i + 1) * 2 * cnt
        
    return answer