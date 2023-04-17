# 20230418
n = int(input())
count = n

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        # 바로 뒤에 중복되는 문자열이 있는지 확인
        if word[i] == word[i+1]:
            pass
        # 비교하고자 하는 문자 뒤 모든 문자열에서 중복이 있는지 확인
        elif word[i] in word[i+1:]: 
            count -= 1
            break
        
print(count)