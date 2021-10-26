# 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며,
# 두 수가 모두 2 이상인 경우에는 곱하면 된다.

data = input()

result = int(data[0])

for i in data[1:]:
    num = int(i)
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)