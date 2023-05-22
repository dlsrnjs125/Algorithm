def solution(wallpaper):
    # 시작좌표 -> 가장 왼쪽에 있는 파일의 x좌표 선택, 가장 위에 y좌표 선택
    # 끝좌표 -> 가장 오른쪽에 있는 파일의 x좌표 선택, 가장 아래에 y좌표 선택
    result = [50, 50, 0, 0]
    
    for yi, y in enumerate(wallpaper):
        for xi, x in enumerate(y):
            if x == "#":
                result = [min(result[0], yi), min(result[1], xi)
                        , max(result[2], (yi+1)), max(result[3], (xi+1))]
                              
    return result
    