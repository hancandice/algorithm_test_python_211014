import math

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")

# 에라스토테네스의 체 알고리즘은 매우 빠르게 동작하기 때문에 다수의 소수를 찾아야 하는 문제에서 자주 사용된다. 다만, 메모리가 많이 필요하다는 단점이 있다.
# 알고리즘을 수행할 때 N의 크기만큼 리스트를 할당해야 하기 때문이다.
