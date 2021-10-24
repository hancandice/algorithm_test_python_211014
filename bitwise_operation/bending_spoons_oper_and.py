# I will write an algorithm to solve this problem, using Python.
# Here's my solution:

import sys

sys.setrecursionlimit(1500)
# RecursionError: maximum recursion depth exceeded in comparison may occur, so it need be dealt with with this line.

a, b = map(int, input().split())  # Get input a and b from user.

start = 0


def oper_and(a, b):
    global start
    start = a
    if b == start:
        return start

    return b & oper_and(a, b - 1)


# c(a,b) requires bitwise operation of all consecutive numbers between a and b,
# so recursion is used in this function oper_and to sequentially perform bitwise operations in a top-down manner.

def c(a, b):
    answer = oper_and(a, b)
    answer = str(bin(answer))[2:]
    return answer


# The final result value should be expressed as a binary number.
# Since "0b" is added in front of the binary number, it should be deleted.

print(c(a, b))

