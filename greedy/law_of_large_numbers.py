# 큰 수의 법칙(law of large numbers, LLN)은 경험적 확률과 수학적 확률 사이의 관계를 나타내는 법칙으로,
# 표본집단의 크기가 커지면 그 표본평균이 모평균에 가까워짐을 의미한다.
# 따라서 취합하는 표본의 수가 많을수록 통계적 정확도는 올라가게 된다.

n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

result = 0

# break 로 빠져나갈 때까지 무한 반복
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break

    result += second
    m -= 1

print(result)
