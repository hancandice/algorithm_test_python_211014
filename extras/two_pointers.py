# 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
# 투 포인터 알고리즘을 이용하여 '특정한 합을 가지는 부분 연속 수열 찾기' 문제를 풀 수 있다
# 리스트 내 원소에 음수 데이터가 포함되어 있는 경우에는 투 포인터 알고리즘으로 문제를 해결할 수 없다

n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
