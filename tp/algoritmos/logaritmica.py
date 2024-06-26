def logarithmic_time(n):
    lst = list(range(n))
    target = n - 1
    low, high = 0, len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
