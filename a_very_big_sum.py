#!/bin/python3

import math
import os
import random
import re
import sys

def is_constraints(ar):
    is_true = False
    n = len(ar)
    for i in range(n):
        if (1 <= n) and (n <= 10):
            if (0 <= int(ar[i])) and (int(ar[i]) <= math.pow(10, 10)):
                is_true = True
    return is_true

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    total = 0
    
    if is_constraints(ar):
        for a in ar:
            total += a

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(fptr.write(str(result) + '\n'))

    fptr.close()
