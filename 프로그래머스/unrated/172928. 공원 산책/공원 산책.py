def solution(park, routes):
    
    row, col = 0, 0 # 현재 위치
    park_row, park_col = len(park), len(park[0]) # park 크기
    move = {"E" : (0, 1), "W" : (0, -1), "S" : (1, 0), "N" : (-1, 0)}
    
    # 시작 위치 찾기
    for i, row in enumerate(park):
        if "S" in row:
            row, col = i, row.find("S")
            break
    
    for route in routes:
        mov_r, mov_c = move[route[0]] # 입력받은 움직임 방향
        new_r, new_c = row, col # 적용 후 위치 저장
        for _ in range(int(route[2])):
            # 한칸씩 움직이며, 장애물이 잇는지 판단
            if (0 <= new_r + mov_r < park_row and 0 <= new_c + mov_c < park_col 
                and park[new_r+mov_r][new_c+mov_c] != "X"):
                new_r, new_c = new_r+mov_r, new_c+mov_c
            else:
                new_r, new_c = row, col
                break
        row, col = new_r, new_c # 위치 업데이트
    
    return [row, col]