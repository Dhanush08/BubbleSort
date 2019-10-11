import random


def array(n):
    a = [random.randint(1, 100) for _ in range(n)]
    return a


def bubble_sort(a, n):
    for k in range(1, n):
        flag = True
        for i in range(n - k):
            if a[i] > a[i + 1]:
                swap(a, i, i + 1)
                flag = False
        if flag:
            break
    return a


def swap(a, x, y):
    a[x], a[y] = a[y], a[x]


n = random.randint(50, 60)
print(bubble_sort(array(n), n))
