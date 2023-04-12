

array_1 = [1, 5, 6, 8, 9, 3]


def quicksort(arr):
    # set base case
    if len(arr) < 2:
        return arr

    # set recursive case
    else:
        # choose the first element of array as pivot
        pivo = arr[0]
        # write all elements of array smaller than pivot to a new array
        left = [i for i in arr[1:] if i <= pivo]
        # write all elements of array greater than pivot to a new array
        right = [i for i in arr[1:] if i > pivo]
        # return smaller elements, pivot, and greater elements
        return quicksort(left) + [pivo] + quicksort(right)


print(quicksort(array_1))
