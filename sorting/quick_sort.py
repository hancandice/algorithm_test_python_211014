# 퀵 정렬은 정렬 알고리즘 중에서 가장 많이 사용되는 알고리즘
# 퀵 정렬은 기준(pivot)을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다. -> Hoare Partition

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = pivot + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[right], arr[pivot] = arr[pivot], arr[right]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
