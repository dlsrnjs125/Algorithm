# 20230320
document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        result += 1
        # 동시에 셀수는 없기 때문에
        index += len(word)
    else:
        index += 1
        
print(result)