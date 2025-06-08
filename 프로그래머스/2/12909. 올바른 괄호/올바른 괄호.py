def solution(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
                
    return stack == [] # stack 이 빈배열이 아니면 False 출력