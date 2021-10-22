v = []

for i in range(3):
    v.append(list(map(int, input().split())))


def find_rectangular_coordinates(arr):
    result = [arr[0][0] ^ arr[1][0] ^ arr[2][0], arr[0][1] ^ arr[1][1] ^ arr[2][1]]
    return result


print(find_rectangular_coordinates(v))
