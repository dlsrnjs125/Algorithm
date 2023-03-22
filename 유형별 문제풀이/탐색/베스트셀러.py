# 20230322
n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
        
target = max(books.values()) # 가장 높은 숫자를 저장
result = []

# 가장 많이 팔린 책을 result에 저장
for book, number in books.items():
    if number == target:
        result.append(book)
        
print(sorted(result)[0])