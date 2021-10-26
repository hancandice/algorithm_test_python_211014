import math

a, b = map(int, input().split())


def oper_and(a, b):
    power = 0
    while True:
        if math.pow(2, power) <= a < math.pow(2, power + 1):
            break
        else:
            power += 1

    if b < math.pow(2, power + 1):
        return int(math.pow(2, power))
    else:
        return 0


def c(a, b):
    answer = oper_and(a, b)
    answer = str(bin(answer))[2:]
    return answer


print(c(a, b))
