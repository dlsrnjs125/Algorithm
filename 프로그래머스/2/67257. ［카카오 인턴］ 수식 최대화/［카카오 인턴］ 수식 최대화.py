def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    
    for op in operations:
        a = op[0]    # 우선순위 1 연산자
        b = op[1]    # 우선순위 2 연산자
        temp_list = []

        # 연산자 우선순위 별 계산식 만들기
        # 1) 우선순위가 1인 연산자를 기준으로 나누기
        for e in expression.split(a):
            
            # 2) 우선순위가 2인 연산자를 기준으로 나누고 괄호 씌우기
            temp = [f"({i})" for i in e.split(b)]

            # 3) 위에서 나눈 값들을 우선순위가 2인 연산자로 다시 연결하기
            temp_list.append(f'({b.join(temp)})')

        # 우선순위가 1인 연산자로 다시 연결한 최종 계산식을 실행한 값의 절댓값 구하기
        answer.append(abs(eval(a.join(temp_list))))
        
    return max(answer) # 제일 큰 값
