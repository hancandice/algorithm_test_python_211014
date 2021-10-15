n = int(input())
count = 0
coin_types = list(map(int, input().split()))
coin_types.sort(reverse=True)

for coin in coin_types:
    count += n // coin
    n %= coin

print(coin_types)
print(count)


# 거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는
# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 "배수"이므로,
# 작은 단위들의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.


