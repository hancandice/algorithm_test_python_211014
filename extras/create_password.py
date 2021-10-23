# 조합 알고리즘의 문제 유형
# 길이가 L인 모든 암호 조합을 확인한 뒤에, 최소 1개의 모음과 최소 2개의 자음이 있는 경우만 출력하면 된다

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')

l, c = map(int, input().split())

array = input().split()
array.sort()

for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    if 1 <= count <= l - 2:
        print("".join(password))
