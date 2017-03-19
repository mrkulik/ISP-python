import readfromfile


def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst


def mergesort(lst):
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst


def qsort(lst):
    if not lst:
        return []
    else:
        pivot = lst[0]
        lesser = qsort([x for x in lst[1:] if x < pivot])
        greater = qsort([x for x in lst[1:] if x >= pivot])
        return lesser + [pivot] + greater


def radix(lst):
    A = lst
    length = len(str(max(A)))
    rang = 10
    for i in range(length):
        B = [[] for k in range(rang)]
        for x in A:
            figure = x // 10 ** i % 10
            B[figure].append(x)
        A = []
        for k in range(rang):
            A = A + B[k]
    return A


def start():
    a = readfromfile.read_from_file('sort.txt').split()
    for i in range(len(a)):
        a[i] = int(a[i])
    print('Entered array:', a)
    print('MergeSort', mergesort(a))
    print('RadixSort', radix(a))
    print('QuickSort', qsort(a))


start()