"""Calculate fibonacci value at index `n` using recursion"""


def fibonacci(n):
    """f(n) = f(n-1) + f(n-2)"""
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print('Fibonacci at 5:',  fibonacci(8))
    """
    Fibonacci at 5: 21
    """