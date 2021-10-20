# 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 후에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.

n, m = map(int, input().split())

graph = []
for i in range(n):
    # 입력값이 띄어쓰기로 나누어지지 않고 붙어있는 경우 -> list(map(int, input()))
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True

    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
