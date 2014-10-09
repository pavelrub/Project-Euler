__author__ = 'Pavel Rubinson'

""" Problem description:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    """ Check if a given string is a palindrome
    """
    if len(n) == 0:
        return True
    elif n[0] == n[-1]:
        return is_palindrome(n[1:-1])
    else:
        return False


def largest_pali():
    """ Find the maximum palindrome which is a product of 3-digit numbers
    """
    max = -1
    for i in range(100, 1000):
        for j in range(i + 1, 1000):
            prod = i * j
            if is_palindrome(str(prod)) and prod > max:
                max = prod
    return max


print(largest_pali())