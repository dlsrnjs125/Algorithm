def solution(arr):
    count = -1
    raw = arr.copy()
    while 1:
        raw = arr.copy()
               
        for i in range(len(arr)):
            if arr[i] >=50 and arr[i]%2==0:
                arr[i]=arr[i]//2
            elif arr[i]<=50 and arr[i]%2==1:
                arr[i]=arr[i]*2+1
        count +=1
        
        # 이전 배열과 변환배열이 같다면
        a = 0
        
        for i in range(len(arr)):   
            if arr[i] == raw[i]:
                a +=1
                
        if len(arr)== a:
            return count # 변환횟수 return 