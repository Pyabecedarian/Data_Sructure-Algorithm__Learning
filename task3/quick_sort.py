"""
Quick Sort
"""


def quick_sort(l):
    """Main function of Quick Sort"""
    return _quick_sort(l, 0, len(l) - 1)


def _quick_sort(l, start, end):
    """Helper function of Quick Sort"""
    if start < end:
        split_point = partition(l, start, end)

        _quick_sort(l, start, split_point - 1)
        _quick_sort(l, split_point + 1, end)

    return l


def partition(l, start, end):
    pivot = l[start]

    p1, p2 = start + 1, end

    while p1 <= p2:
        if l[p1] <= pivot:
            p1 += 1
        elif l[p2] >= pivot:
            p2 -= 1
        else:
            l[p1], l[p2] = l[p2], l[p1]
            p1 += 1
            p2 -= 1

    l[start], l[p2] = l[p2], l[start]

    return p2


if __name__ == '__main__':
    a = [9, 12, 3, 1, 5, 8, 10, 2, 1]
    print(quick_sort(a))
