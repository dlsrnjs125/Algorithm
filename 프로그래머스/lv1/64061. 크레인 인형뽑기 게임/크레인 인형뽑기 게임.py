def solution(board, moves):
    answer = []
    bucket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]
                    bucket = bucket[:-2]
                break
    
    return len(answer) * 2