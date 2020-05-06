"""Optional questions for Lab 1"""

# While Loops

def power_loop(a, b):
    """Compute a to the power b
    >>> power_loop(0, 0) # 0 ** 0 = 1
    1
    >>> power_loop(3, 0) # 3 ** 0 = 1
    1
    >>> power_loop(0, 3) # 0 ** 3 = 0
    0
    >>> power_loop(2, 5) # 2 ** 5 = 32
    32
    >>> power_loop(4, 9) # 4 ** 9 = 262144
    262144
    """
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b % 2 == 0:
        temp = power_loop(a, b / 2)
        return temp * temp
    else:
        return a * power_loop(a, b - 1)


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    elif k > n:
        return falling(n, n)
    else:
        return n * falling(n-1, k-1)


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    if n < 10:
        return False
    q, r = n // 10, n % 10
    if  r != 8:
        return double_eights(q)
    else:
        t, d = q // 10, q % 10
        if d == 8:
            return True
        else:
            return double_eights(t)

# Boolean Operators

def right_triangle(a, b, c):
    """Determine whether a, b, and c can be sides of a right triangle
    >>> right_triangle(1, 1, 1)
    False
    >>> right_triangle(5, 3, 4)
    True
    >>> right_triangle(8, 10, 6)
    True
    """
    is_triangle = (a + b > c) and (b + c > a) and (a+c) > b
    is_right = (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b)
    return is_triangle and is_right 
    
