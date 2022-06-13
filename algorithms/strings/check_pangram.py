"""
Algorithm that checks if a given string is a pangram or not
"""

def check_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return all(ch in input_string.lower() for ch in alphabet) 