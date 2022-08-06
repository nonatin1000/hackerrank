"""
supose you are give two strings and t string t is generated randomly shuffling and them adding one more letter at a radom position. Return the letter that was added to t

exemple 1
s = "abcd", t="ceadb"
e

exemple 2
s = "abbdd", t="dabadb"
a

exemple 3
s = "", t="y"
 "y"

s = "aaaa", t="aabaa"
"b"

cad was produced by random shuffling abcd and e was added in as the second letter
"""

import collections


def findTheDifference(s: str, t: str) -> str:
    c = collections.Counter(t) - collections.Counter(s)
    return c.most_common(1)[0][0]


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(findTheDifference(s, t))
