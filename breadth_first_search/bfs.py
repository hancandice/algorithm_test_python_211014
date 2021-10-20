# 너비 우선 탐색 알고리즘인 BFS 는 큐 자료구조에 기초한다.
# 탐색을 수행하는 데 있어 O(N)의 시간이 소요된다.
# 일반적인 경우 실제 수행 시간은 DFS 보다 좋은 편

from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * (len(graph))


def bfs(_graph, start, _visited):
    queue = deque([start])

    _visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not _visited[i]:
                queue.append(i)
                _visited[i] = True


bfs(graph, 1, visited)
