"""
Given two strings S and T, determine if they are both one edit distance apart.
"""


def is_one_edit(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) > len(t):
        return is_one_edit(t, s)
    if len(t) - len(s) > 1 or t == s:
        return False
    return next(
        (
            s[i + 1 :] == t[i + 1 :] or s[i:] == t[i + 1 :]
            for i in range(len(s))
            if s[i] != t[i]
        ),
        True,
    )


def is_one_edit2(s, t):
    l1, l2 = len(s), len(t)
    if l1 > l2:
        return is_one_edit2(t, s)
    if len(t) - len(s) > 1 or t == s:
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            s = s[:i]+t[i]+s[i+1:] if l1 == l2 else s[:i]+t[i]+s[i:]
            break
    return s in [t, t[:-1]]
