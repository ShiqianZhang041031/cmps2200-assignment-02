"""
CMPS 2200 Assignment 2.
See assignment-02.pdf for details.

Name: Shiqian Zhang
"""

import time


class BinaryNumber:
    """A simple representation of a nonnegative integer in binary."""

    def __init__(self, n):
        self.decimal_val = n
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        return (
            'decimal=%d binary=%s'
            % (self.decimal_val, ''.join(self.binary_vec))
        )


def quadratic_multiply(x, y):
    """
    Multiply two BinaryNumbers using the standard divide-and-conquer
    algorithm with four recursive multiplications.
    """

    def multiply(a, b):
        if a == 0 or b == 0:
            return 0

        n = max(a.bit_length(), b.bit_length())

        if n <= 1:
            return a * b

        # Make n even so the two halves have equal length.
        if n % 2 == 1:
            n += 1

        half = n // 2
        mask = (1 << half) - 1

        a_left = a >> half
        a_right = a & mask

        b_left = b >> half
        b_right = b & mask

        left_product = multiply(a_left, b_left)
        outer_product = multiply(a_left, b_right)
        inner_product = multiply(a_right, b_left)
        right_product = multiply(a_right, b_right)

        return (
            (left_product << (2 * half))
            + ((outer_product + inner_product) << half)
            + right_product
        )

    return multiply(x.decimal_val, y.decimal_val)


def subquadratic_multiply(x, y):
    """
    Multiply two BinaryNumbers using the Karatsuba-Ofman algorithm,
    which uses three recursive multiplications.
    """

    def multiply(a, b):
        if a == 0 or b == 0:
            return 0

        n = max(a.bit_length(), b.bit_length())

        if n <= 1:
            return a * b

        if n % 2 == 1:
            n += 1

        half = n // 2
        mask = (1 << half) - 1

        a_left = a >> half
        a_right = a & mask

        b_left = b >> half
        b_right = b & mask

        high = multiply(a_left, b_left)
        low = multiply(a_right, b_right)

        middle = (
            multiply(a_left + a_right, b_left + b_right)
            - high
            - low
        )

        return (
            (high << (2 * half))
            + (middle << half)
            + low
        )

    return multiply(x.decimal_val, y.decimal_val)


def time_multiply(x, y, f):
    start = time.time()

    # multiply two numbers x, y using function f
    f(x, y)

    return (time.time() - start) * 1000


def compare_multiply():
    """
    Compare empirical runtimes for the quadratic and Karatsuba
    multiplication algorithms at several input sizes.
    """

    bit_sizes = [8, 16, 32, 64, 128, 256]
    results = []

    for bits in bit_sizes:
        # An integer consisting of 'bits' one-bits.
        value = (1 << bits) - 1

        x = BinaryNumber(value)
        y = BinaryNumber(value)

        quadratic_time = time_multiply(
            x,
            y,
            quadratic_multiply
        )

        subquadratic_time = time_multiply(
            x,
            y,
            subquadratic_multiply
        )

        results.append(
            (
                bits,
                quadratic_time,
                subquadratic_time
            )
        )

    return results
