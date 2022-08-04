"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example
n=7
ar=[1,2,1,2,1,3,2]

There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs

Input Format

The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers,ar[i] , the colors of the socks in the pile.

Constraints
1 <= n <= 100
1 <= ar[i] <= 100 where 0 <= i < n

Sample Input

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
Sample Output

3
Explanation


"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    sock_dict = {}
    for sock in ar:
        if sock in sock_dict:
            sock_dict[sock] += 1
        else:
            sock_dict[sock] = 1
    return sum(value // 2 for value in sock_dict.values())


# def sockMerchant(n, ar):
#     # Write your code here
#     # Create a dictionary to store the number of socks of each color
#     sock_dict = {}
#     # Loop through the array and add the number of socks of each color to the dictionary
#     for sock in ar:
#         if sock in sock_dict:
#             sock_dict[sock] += 1
#         else:
#             sock_dict[sock] = 1
#     # Create a variable to store the number of pairs of socks
#     pairs = 0
#     # Loop through the dictionary and add the number of pairs of socks to the variable
#     for key in sock_dict:
#         pairs += sock_dict[key] // 2
#     return pairs


if __name__ == "__main__":
    fptr = open("soc.txt", "w")

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print("result = ", result)

    fptr.write(str(result) + "\n")

    fptr.close()
