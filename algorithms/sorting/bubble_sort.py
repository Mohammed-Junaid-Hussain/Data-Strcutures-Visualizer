
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            # show comparison
            yield arr.copy(), (j, j + 1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                # show swap
                yield arr.copy(), (j, j + 1)
        if not swapped:
            break
    yield arr.copy(), ()
