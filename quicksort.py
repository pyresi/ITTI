

array_1 = [1, 5, 6, 8, 9, 3]


def quicksort(arr):

    if len(arr) < 2:
        return arr

    else:
        pivo = arr[0]

        left = [i for i in arr[1:] if i <= pivo]
        right = [i for i in arr[1:] if i > pivo]

        return quicksort(left) + [pivo] + quicksort(right)


print(quicksort(array_1))
