#!/bin/python3
# Complete the plusMinus function below.
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    amount_p = 0
    amount_n = 0
    amount_z = 0

    for i in range(n):
        if 0 < n and n <= 100:
            if -100 <= arr[i] and arr[i] <= 100:
                if arr[i] < 0:
                    amount_n += 1
                elif arr[i] > 0:
                    amount_p += 1
                else:
                    amount_z += 1

    print(round(amount_p / n, 6))
    print(round(amount_n / n, 6))
    print(round(amount_z / n, 6))


arr = [1, 2, 3, -1, -2, -3, 0, 0]

plusMinus(arr)

