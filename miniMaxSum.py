"""
    Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

    Example
    arr = [1, 3, 5, 7, 9]
    The minimum sum is 1+3+5+7=16  and the maximum sum is 3+5+7+9=24. The function prints

    16 24
    Function Description

    Complete the miniMaxSum function in the editor below.

    miniMaxSum has the following parameter(s):

    arr: an array of 5 integers
    Print

    Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

    Input Format

    A single line of five space-separated integers.

    Constraints
    1 <= arr[i] <= 10^9

    Output Format

    Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

    Sample Input

    1 2 3 4 5
    Sample Output

    10 14
    Explanation

    The numbers are , , , , and . Calculate the following sums using four of the five integers:

    Sum everything except , the sum is .
    Sum everything except , the sum is .
    Sum everything except , the sum is .
    Sum everything except , the sum is .
    Sum everything except , the sum is .    
    
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
