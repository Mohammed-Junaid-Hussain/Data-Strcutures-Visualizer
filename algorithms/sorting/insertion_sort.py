
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Focus on the key
        yield arr.copy(), (i,)
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            # Show shifting and comparison
            yield arr.copy(), (j, j + 1)
        arr[j + 1] = key
        # Show insertion
        yield arr.copy(), (j + 1,)
    yield arr.copy(), ()
