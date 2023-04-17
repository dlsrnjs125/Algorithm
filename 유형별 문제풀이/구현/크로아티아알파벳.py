# 20230417
n = input()
count = len(n)
cro_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(n)):
    if len(n) < 2: # 문자열의 길이가 2보다 작을 때
        count = len(n)
    elif len(n) == 2: # 문자열의 길이가 2일 때
        if (n[i-1] + n[i]) in cro_alphabet:
            count = 1
    # 문자열의 길이가 3이상일 때
    elif (n[i-2] + n[i-1] + n[i]) in cro_alphabet: # 연달아 3개의 문자가 크로아티아 알파벳
        count -= 2
    elif (n[i-1] + n[i]) in cro_alphabet: # 연달아 2개의 문자가 크로아티아 알파벳
        count -= 1
        
print(count)