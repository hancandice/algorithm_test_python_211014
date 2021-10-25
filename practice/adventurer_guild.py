# 그리디 유형의 문제에서는 '현재 상황에서 특정한 기준에 따라 가장 좋아 보이는 것만을 선택' 하여 최적의 해를 구해야 한다.

N = int(input())
data = list(map(int, input().split()))
data.sort()

member = 0
count = 0

for x in data:
    member += 1

    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도와 같다면, 그룹 결성
    if member == x:
        count += 1
        member = 0

print(count)