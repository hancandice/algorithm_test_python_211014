# 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램
# 연산 횟수는 이동 횟수에 비례 -> 시간 복잡도는 O(N)
# 일련의 명령에 따라 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류됨. 구현이 중요한 대표적인 문제 유형

n = int(input())
plans = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue

            x, y = nx, ny

print(x, y)
