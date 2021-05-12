#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can execute
    only two operations in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    * Returns an integer
    * If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    optn = 0
    aux = 2
    while (aux <= n):
        if not (n % aux):
            n = int(n / aux)
            optn += aux
            aux = 1
        aux += 1
    return optn
    