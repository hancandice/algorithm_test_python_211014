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

    while (sum_value + (q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        previous = now
        length -= 1

    result = sorted(q, key=lambda x: x[1])
    index = (k - sum_value) % length
    answer = result[index][1]
    return answer


print(solution(food_times, k))
