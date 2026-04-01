a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

print(1 if a_math > b_math and a_eng > b_eng else 0)