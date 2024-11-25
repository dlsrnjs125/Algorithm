def solution(myStr):
    answer = []
    
    answer = myStr.replace('a',' ').replace('b',' ').replace('c',' ')
    answer = answer.split()

    if not answer:
        answer = ["EMPTY"]
    
    return answer