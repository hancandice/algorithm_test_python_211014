# 사전에 정렬된 A, B 리스트 선언
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n + m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복한다
while i < n or j < m:
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1

    else:
        result[k] = b[j]
        j += 1

    k += 1

for i in result:
    print(i, end=" ")

# '정렬되어 있는 두 리스트의 합집합' 알고리즘의 경우, 병합 정렬과 같은 일부 알고리즘에서 사용되고 있다.
