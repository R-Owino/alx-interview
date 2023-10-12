#!/usr/bin/python3
'''
Contains a function minOperations()
'''


def minOperations(n: int) -> int:
    '''
    Calculates the fewest number of opeations needed to result in
    exactly n H characters

    Args:
        n (int): the number of H characters after the operations are complete

    Return:
        Number of operations taken to result in n H characters
    '''
    # check if n is imposible to achieve
    if n <= 1:
        return 0

    # current # of H characters
    H_chars = 1
    # current number of operations
    operations = 0
    # track # of copied chars
    copied_chars = 0

    # loop until we have 'n''H characters in the file
    while H_chars < n:
        # check for copy all and paste in each iteration
        if n % H_chars == 0:
            # If 'n' is divisible by H_chars, we can perform a Copy All op
            copied_chars = H_chars
            # performed a copy, so operations goes up by 1
            operations += 1

        # If 'n' is not divisible by H_chars, we can only Paste
        H_chars += copied_chars
        # performed a paste, so operations goes up by 1
        operations += 1

    # return number of operations
    return operations
