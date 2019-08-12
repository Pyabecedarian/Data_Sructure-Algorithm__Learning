"""
Sqrt(a):

    Method 1:  Newton Method:
    <==>  x = (a)^1/2  <==>  x^2 = a  <==>  f(x) = x^2 - a = 0

    Tyler expansion：
          f(x) = f(x0) + f'(x0)(x-x0)  <==>  x = x0 - f(x0) / f'(x0)
    <==>  x = 1/2 * (x0 + a/x0)

    Method 2:  Binary Search
    <==>  x ∈ [0, a)  <==>  Binary Search
"""


def sqrt_newton(a):
    """Newton Method"""
    epsilon = 0.001  # error
    x = 10.  # randomly initialized value, but not 0
    n = 0    # iteration number

    while x * x - a > epsilon or a - x * x > epsilon:
        x = 1 / 2 * (x + a / x)
        n += 1

    return x, n


def sqrt_binary_search(a):
    """Binary Search"""
    epsilon = 0.001
    x = 10.
    n = 0

    low = 0
    high = a
    while x * x - a > epsilon or a - x * x > epsilon:
        n += 1
        if x * x < a:
            low = x
        else:
            high = x

        x = (high + low) / 2

    return x, n


if __name__ == '__main__':
    print(sqrt_newton(789))         # (28.08914381289573, 5)
    print(sqrt_binary_search(789))  # (28.089148193597794, 25)
