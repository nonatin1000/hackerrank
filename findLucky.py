"""
exemple
arr = [1, 2, 3, 10, 10, 10, 5, 6]
3
return amount time the number repeat in list
"""
import collections


def findLucky(arr):
    return collections.Counter(arr).most_common(1)[0][1]


arr = [1, 2, 3, 6, 6, 8, 9, 6]
print(findLucky(arr))
