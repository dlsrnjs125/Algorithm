def solution(players, callings):
    player = dict()
    # enumerate -> 인덱스와 값을 같이 저장
    for i, v in enumerate(players):
        player[v] = i
    
    # pre = 이름 부른 앞 사람
    # post = 이름 부른 사람
    for name in callings:
        pre, post = player[name] - 1, player[name]
        player[players[pre]], player[players[post]] = post, pre
        players[pre],players[post] = players[post], players[pre]
    
    return players