""" 
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1  meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

Example

x1=2
v1=1
x2=1
v2=2


After one jump, they are both at x=3, (x1+v1=2+1, x2+v2=1+2), so the answer is YES.

Function Description

Complete the function kangaroo in the editor below.

kangaroo has the following parameter(s):

int x1, int v1: starting position and jump distance for kangaroo 1
int x2, int v2: starting position and jump distance for kangaroo 2
Returns

string: either YES or NO
Input Format

A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.

Constraints
0<=x1<x2<=10000
1<=v1<=10000
1<=v2<=10000

Sample Input 0

0 3 4 2
Sample Output 0

YES
Explanation 0

The two kangaroos jump through the following sequence of locations:

image

From the image, it is clear that the kangaroos meet at the same location (number  12  on the number line) after same number of jumps (4 jumps), and we print YES.

Sample Input 1

0 2 5 3
Sample Output 1

NO
Explanation 1

Explanation 1

The second kangaroo has a starting location that is ahead (further to the right) of the first kangaroo's starting location (i.e., x2>x1).
Because the second kangaroo moves at a faster rate (meaning v2>v1) and is already ahead of the first kangaroo, the first kangaroo will never be able to catch up.
Thus, we print NO.

"""

# x1 = 43 -> 48 -> 53 -> 58
# v1 = 5
# x2 = 49 -> 52 -> 55 -> 58
# v2 = 3


def kangaroo(x1, v1, x2, v2):
    if v2 <= v1:
        for i in range(10000):
            if x1 + v1 * i == x2 + v2 * i:
                return "YES"
    return "NO"


if __name__ == "__main__":
    fptr = open("kanguro.txt", "w")

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
    print("result: ", result)
    fptr.write(result + "\n")

    fptr.close()
