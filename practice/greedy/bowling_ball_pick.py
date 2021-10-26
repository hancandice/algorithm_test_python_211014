n, m = map(int, input().split())
bowling_balls = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if bowling_balls[i] != bowling_balls[j]:
            count += 1

print(count)
