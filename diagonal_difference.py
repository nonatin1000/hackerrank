#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

arr = list([[11, 2, 4],
            [4,  5, 6],
            [10, 8, -12]])

def diagonalDifference(arr):
    sum_dp = 0
    sum_ds = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            # pego a diagonal secundária, somo i + j e diminuo pelo tamanho do array de 1
            if i + j == n - 1:
                sum_ds += arr[i][j]

            # diagonal principal
            if i == j:
                sum_dp += arr[i][j]

    print('soma diagonal principal.: ', sum_dp)
    print('soma diagonal secundaria: ', sum_ds)
    return abs(sum_dp - sum_ds)

print(diagonalDifference(arr))

