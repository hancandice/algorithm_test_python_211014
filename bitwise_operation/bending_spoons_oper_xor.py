# First, in the bitwise exclusive OR operation, there is no difference in the result depending on the order of the bitwise exclusive OR operation.
# In other words, if we reverse the order of calculation in the expression given in the above example,
# 3 ⊕ 5 ⊕ 1 = (3 ⊕ 5) ⊕ 1 = 6 ⊕ 1 = 3 ⊕ (5 ⊕ 1) = 3 ⊕ 4 = 7 also holds.
#
# Therefore, the result of sequentially creating sub-arrays by increasing the size of the sub-array by 1, and performing all bitwise exclusive OR operations on them, is the same as the result of performing bitwise exclusive OR operation on each element in the array by a certain number with itself according to a certain rule.
#
# To make it clear, let me give you an example.
#
# f([3, 5, 1]) = (3) ⊕ (5) ⊕ (1) ⊕ (3 ⊕ 5) ⊕ (5 ⊕ 1) ⊕ (3 ⊕ 5 ⊕ 1) = 3 ⊕ 5 ⊕ 1 ⊕ 6 ⊕ 4 ⊕ 7 = 2
#
# In the above equation, 3 appears 3 times, 5 appears 4 times, and 1 appears 3 times.
# This result can be said to be the same as the result of 3 times of bitwise exclusive OR operation on 3, 4 times of bitwise exclusive OR operation on 5, and 3 times of bitwise exclusive OR operation on 1.
#
# Considering these rules, when the size of the array is even, all numbers must be counted even times, and the total result is 0.
#
# Therefore, if we consider only the case where the size of the array is odd, an element with an even index appears odd numbered times, and an element with an odd index appears even number of times.
#
# In the end, the only thing to consider is whether the size of the array is odd, and if it is odd, calculating the result value only for elements with even indexes.
#
# In the case of elements with even indices, it calculates itself an odd number of times and its value becomes its own value,
#
# Therefore, the desired value is the value obtained by performing bitwise exclusive OR operation on all elements with even indexes among the array whose length is odd number.
#
# according to what I have been described, I solved the problem using python, and my algorithm is:

from functools import reduce
from operator import xor

X = list(map(int, input().split())) # Receive element input from the user using spaces as delimiters, and make it into a list.


def f(array):
    if len(array) % 2 == 0:
        return 0

    even_indices = []

    for x in range(len(array)):
        if x % 2 == 0:
            even_indices.append(array[x])

    return reduce(xor, map(int, even_indices))


print(f(X))
