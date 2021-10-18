# array = [i for i in range(20) if i % 2 == 1]
#
# print(array)

# 2차원 리스트를 초기화할 떄 매우 유리
# N * M 크기의 2차원 리스트 초기화
# n = 3
# m = 4
# array = [[0] * m for _ in range(n)]

# 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야 한다.

n = 3
m = 4
# array = [[0] * m] * n
# 이는 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문이다.
# 따라서 특정한 크기를 가지는 2차원 리스트를 초기화할 때에는 리스트 컴프리헨션을 이용해야 한다.

array = [[0] * m for _ in range(n)]

array[1][1] = 5

print(array)

# 파이썬에서 특정한 값의 원소를 모두 제거하는 방법
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set 에 포함되지 않은 값 만을 저장
result = [i for i in a if i not in remove_set]
print(result)