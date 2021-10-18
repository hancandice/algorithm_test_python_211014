# 흔히 개발할 때 프로그래밍 언어의 문법에 능숙하고 코드 작성 속도가 빠른 사람을 보고 '피지컬이 좋다'라고 이야기하는데,
# 구현 유형의 문제는 그런 의미에서 피지컬을 요구하는 문제라고 할 수 있다.

# 나이트의 현재 위치가 주어지면 현재 위치에서 이동 경로를 더한 다음, 8 * 8 좌표 평면에 있는지 확인하면 된다.

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (1, -2), (-1, -2), (2, 1), (2, -1), (1, 2), (-1, 2)]

count = 0
for step in steps:
    next_row = row + step[1]
    next_column = column + step[0]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)
