# 20230305
test_case = int(input())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-': # 백스체이스
            if left_stack:
                left_stack.pop()
        elif i == '<': # 왼쪽 화살표
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>': # 오른쪽 화살표
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack)) # left_stack에 right_stack을 뒤집어서 끝에다가 모든 항목 넣기
    print(''.join(left_stack))