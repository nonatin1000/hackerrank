#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    resul = [0, 0]
    for i in range(len(a)):
        print('alice ', a[i])
        print('bob ', b[i])
        if a[i] > b[i]:
            resul[0] += 1
        elif a[i] < b[i]:
            resul[1] += 1
        else:
            continue

    return resul

a = [5, 6, 7]
b = [3, 6, 10]

print(compareTriplets(a, b)) 