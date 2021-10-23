# 구간 합 문제는 여러 개의 쿼리(Query)로 구성되는 문제 형태로 출제되는 경우가 많다.
# 다수의 구간에 대해서 합을 각각 구하도록 요구된다.
# M개의 쿼리가 존재한다고 가정해 보면, 각 쿼리는 Left 와 Right 로 구성되며, 이는 [Left, Right] 의 구간을 의미한다.
# 우리가 알고리즘을 설계할 때 고려해야 할 점은 여러 번 사용될 만한 정보는 미리 구해 저장해 놓을수록 유리하다는 것이다.
# 구간 합 계산을 위해 가장 많이 사용되는 기법 : 접두사 합 (Prefix Sum)

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0

prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
