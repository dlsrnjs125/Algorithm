# 20230309
array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='') # end : 줄바꿈하지 않고 뒤에 바로 출력