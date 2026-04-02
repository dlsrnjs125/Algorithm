n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(arr, n):
    # 종료 조건
    if n == 1:
        return arr[0]
    # 마지막 원소와 나머지 최댓값 비교
    return max(arr[n-1], find_max(arr, n-1))

print(find_max(arr, n))