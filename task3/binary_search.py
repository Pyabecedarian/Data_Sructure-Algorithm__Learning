"""
Binary Search
"""


def binary_search(l, item, fuzzy=False):
    """
    If the item is in list `l`, then return it's index, otherwise if fuzzy is False, return -1,
    of if fuzzy is True, return the index of which value is larger then it.
    """

    low = 0
    high = len(l) - 1

    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if l[mid] == item:
            found = True
        else:
            if l[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
    if found:
        return mid
    else:
        if fuzzy:
            if l[mid] > item or mid == len(l) - 1:
                return mid
            else:
                return mid + 1
        else:
            return -1


if __name__ == '__main__':
    #    0  1  2  3  4  5  6  7   8
    a = [1, 1, 2, 3, 5, 8, 9, 10, 12]

    # Accurate search `8`:
    print(binary_search(a, 8))  # 5
    print(binary_search(a, 11, fuzzy=True))

