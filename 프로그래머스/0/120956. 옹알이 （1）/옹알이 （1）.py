def solution(babbling):
    answer = 0
    words = ["aya", "yee", "u", "maa", "wyeoo"]
    
    for i in range(len(babbling)):
        word = str(babbling[i])
        for j in range(len(word)):
            if "aya" in word[0:3]:
                word = word.replace(word[0:3], "")
            elif "ye" in word[0:2]:
                word = word.replace(word[0:2], "")
            elif "woo" in word[0:3]:
                word = word.replace(word[0:3], "")
            elif "ma" in word[0:2]:
                word = word.replace(word[0:2], "")
            elif len(word) == 0:
                answer += 1
                break
            else:
                break
        
    return answer