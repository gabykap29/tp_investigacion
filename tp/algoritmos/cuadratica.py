def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def quadratic_time(n):
    lst = list(range(n, 0, -1))
    bubble_sort(lst)
    return lst
