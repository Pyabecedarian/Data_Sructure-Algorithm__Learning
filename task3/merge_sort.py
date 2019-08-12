"""
Merge Sort
"""


def merge(left, right):
    """Merge two sorted list to one sorted list"""
    res = []
    p1, p2 = 0, 0

    while True:
        if p1 == len(left):
            res.extend(right[p2:])
            break
        elif p2 == len(right):
            res.extend(left[p1:])
            break

        elif left[p1] < right[p2]:
            res.append(left[p1])
            p1 += 1
        else:
            res.append(right[p2])
            p2 += 1

    return res


def merge_sort(l):
    if len(l) == 1:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    return merge(left, right)


if __name__ == '__main__':
    a = [1, 5, 2, 8, 0, 2, 10, 9, 20]
    print(merge_sort(a))
