def prime_check(n):
    """Return True if n is a prime number
    Else return False.
    """

    if n <= 1:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j**2 <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True
