def nth_fib_lists(listA, listB, n):
    p = 2
    while p < n + 1:
        m = listA + listB
        listA = listB
        listB = m
        p += 1
    return listA
