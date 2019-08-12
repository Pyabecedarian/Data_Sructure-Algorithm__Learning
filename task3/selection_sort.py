"""
Selection Sort
"""


def selection_sort(l):
    for selected_index in range(len(l) - 1, 0, -1):

        loc_max_index = 0
        for i in range(1, selected_index):
            if l[i] > l[loc_max_index]:
                loc_max_index = i

        if l[loc_max_index] > l[selected_index]:
            l[loc_max_index], l[selected_index] = l[selected_index], l[loc_max_index]

    return l


if __name__ == '__main__':
    a = [21, 1, 7, 13, 91, 87, 52, 41, 1]
    print(selection_sort(a))