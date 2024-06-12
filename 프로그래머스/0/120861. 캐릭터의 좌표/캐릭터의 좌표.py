def solution(keyinput, board):
    answer = []
    x_lim, y_lim = board[0]//2,board[1]//2 
    x, y = 0, 0
    
    for i in keyinput:
        if i == 'right':
            if x >= x_lim:
                x = x_lim
            else:
                x +=1
        elif i == 'left':
            if x <= -x_lim:
                x = -x_lim
            else:
                x -= 1
        elif i == 'up':
            if y >= y_lim:
                y = y_lim
            else:
                y += 1
        elif i == 'down': 
            if y <= -y_lim:
                y = -y_lim
            else:
                y -= 1
    
    answer = x, y
    return answer