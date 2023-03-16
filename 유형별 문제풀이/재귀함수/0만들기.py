# 20230316
import copy

def reculsive(array, n):
    if len(array) == n:
        # deppcopy -> 배열의 내용이 그대로 copy
        # python에서는 array라는 배열을 공유하기 때문에 pop하는 순간 모든 배열에서 빠져나가기 떄문에
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    reculsive(array, n)
    array.pop()
    
    array.append('+')
    reculsive(array, n)
    array.pop()
    
    array.append('-')
    reculsive(array, n)
    array.pop()
    
test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    # 재귀 함수 -> 연산자 배열 리스트를 만들기 위해
    reculsive([], n-1) 
    # 입력된 정수 배열을 만들기 위해
    integers = [i for i in range(1, n+1)]
    
    for operators in operators_list:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1]) # 정수가 연산자보다 한개 더 많기 때문에
        if eval(string.replace(" ", "")) == 0: # 공백을 제거한 결과를 연산
            print(string)
    print()