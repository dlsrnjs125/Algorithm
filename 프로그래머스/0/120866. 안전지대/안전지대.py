def solution(board):
    answer = 0
    N = len(board)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]
    boom = []
    
    # 지뢰 설치
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                boom.append((i, j)) # 지뢰의 인덱스
    
    # 지뢰가 설치된 주변에 폭탄 설치
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1
    
    # 설치 안된 곳 카운팅
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                answer += 1
    return answer