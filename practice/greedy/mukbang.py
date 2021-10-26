# https://programmers.co.kr/learn/courses/30/lessons/42891\

# 시간이 적게 걸리는 음식부터 확인하는 탐욕적(Greedy) 접근 방식으로 해결할 수 있음
# 모든 음식을 시간을 기준으로 정렬한 후에, 시간이 적게 걸리는 음식부터 제거해 나가는 방식을 이용하자
# 이를 위해 "우선순위 큐"를 이용하여 구현할 수 있다

import heapq

food_times = list(map(int, input().split()))
k = int(input())


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0]) - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])

    return result[(k-sum_value) % length][1]


print(solution(food_times, k))
