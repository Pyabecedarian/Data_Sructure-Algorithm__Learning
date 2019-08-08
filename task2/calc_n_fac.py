def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print(factorial(4))  # 24