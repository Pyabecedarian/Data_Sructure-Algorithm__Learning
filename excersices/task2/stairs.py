from task1.LinkedList import LinkedList


def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairs_v2(n):
    stairs = LinkedList(size=n)
    stairs[0] = 1
    stairs[1] = 2
    for i in range(2, n):
        stairs[i] = stairs[i - 1] + stairs[i - 2]

    return stairs[-1]


if __name__ == '__main__':
    print(climbStairs(5))  # 8
    print(climbStairs_v2(5))  # 8
