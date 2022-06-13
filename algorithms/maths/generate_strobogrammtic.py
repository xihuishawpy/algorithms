"""
A strobogrammatic number is a number that looks
the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
"""

def gen_strobogrammatic(n):
    """
    Given n, generate all strobogrammatic numbers of length n.
    :type n: int
    :rtype: List[str]
    """
    return helper(n, n)

def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append(f"0{middle}0")
        result.extend((f"8{middle}8", f"1{middle}1", f"9{middle}6", f"6{middle}9"))
    return result

def strobogrammatic_in_range(low, high):
    """
    :type low: str
    :type high: str
    :rtype: int
    """
    res = []
    count = 0
    low_len = len(low)
    high_len = len(high)
    for i in range(low_len, high_len + 1):
        res.extend(helper2(i, i))
    for perm in res:
        if len(perm) == low_len and int(perm) < int(low):
            continue
        if len(perm) == high_len and int(perm) > int(high):
            continue
        count += 1
    return count

def helper2(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "8", "1"]
    mids = helper(n-2, length)
    res = []
    for mid in mids:
        if n != length:
            res.append(f"0{mid}0")
        res.extend((f"1{mid}1", f"6{mid}9", f"9{mid}6", f"8{mid}8"))
    return res
