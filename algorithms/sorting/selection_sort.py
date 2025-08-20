
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        # highlight current position
        yield arr.copy(), (i,)
        for j in range(i + 1, n):
            # show comparison with current min
            yield arr.copy(), (min_idx, j)
            if arr[j] < arr[min_idx]:
                min_idx = j
                # show new min
                yield arr.copy(), (min_idx,)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            # show swap
            yield arr.copy(), (i, min_idx)
    yield arr.copy(), ()
