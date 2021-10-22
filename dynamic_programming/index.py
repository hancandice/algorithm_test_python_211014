# 큰 문제를 작은 문제로 나눌 수 있는 경우
# 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일한 경우

d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))
