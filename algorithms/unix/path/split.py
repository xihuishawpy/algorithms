"""
Splitting a path into 2 parts
Example:
Input: https://algorithms/unix/test.py   (for url)
Output:
    part[0]: https://algorithms/unix
    part[1]: test.py

Input: algorithms/unix/test.py          (for file path)
Output:
    part[0]: algorithms/unix
    part[1]: test.py
"""
import os

def split(path):
    split_part = path.rpartition('/')
    return [split_part[0], split_part[2]]
