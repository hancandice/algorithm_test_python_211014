n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def secret_map(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        arr12 = str(bin(i | j)[2:])
        arr12 = arr12.rjust(n, '0')
        arr12 = arr12.replace("1", "#").replace("0", " ")
        answer.append(arr12)
    return answer


print(secret_map(n, arr1, arr2))
