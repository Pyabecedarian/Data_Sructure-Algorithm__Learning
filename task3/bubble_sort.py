"""
Bubble Sort
"""


def bubble_sort(l):
    for num_comparison in range(len(l) - 1, 0, -1):
        for i in range(num_comparison):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]

    return l


def short_bubble_sort(l):

    for num_comparison in range(len(l) - 1, 0, -1):

        no_exchange = True
        for i in range(num_comparison):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                no_exchange = False

        if no_exchange:
            break

    return l


if __name__ == '__main__':
    a = [21, 1, 7, 13, 91, 87, 52, 41]
    print(bubble_sort(a))
    print(short_bubble_sort(a))
