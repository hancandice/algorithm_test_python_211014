# 완전 탐색(Brute Forcing) 유형 : 가능한 모든 경우의 수를 모두 검사해 보는 탐색 방법
# 탐색해야 할 전체 테이터의 개수가 100만 개 이하일 때, 완전 탐색을 사용하면 적절하다.

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            time_string = str(i) + str(j) + str(k)
            if '3' in time_string:
                count += 1

print(count)
