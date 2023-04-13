

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

'''
One potential improvement is to use Python's built-in sorting function sorted()
for smaller arrays rather than recursively calling quickSort. This would reduce
the overhead of function calls and improve performance for small arrays.

In this optimized version, if either the left or right array has less than 10 elements,
sorted() is used to sort it directly. This threshold value can be adjusted based on
performance requirements and input data.
'''
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        if len(left) < 10:
            left = sorted(left)
        else:
            left = quickSort(left)
        if len(right) < 10:
            right = sorted(right)
        else:
            right = quickSort(right)
        return left + [pivot] + right
