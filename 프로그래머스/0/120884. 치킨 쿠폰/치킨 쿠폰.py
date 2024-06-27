def solution(chicken):
    answer = 0
    coupon = 0
    
    while(chicken >= 10):
        coupon = chicken % 10
        service = chicken // 10
        answer += service
        chicken = coupon + service
    
    
    return answer