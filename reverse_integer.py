# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. -2147483648 <-> 2147483647
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
import math
def reverse_integer(x):
    if x == 0:
        return x
    n = int(math.log(abs(x), 10)) + 1 # number of digits
    num = 0
    for place in range(n):
        digit = abs(x) // 10**place % 10
        num += digit * 10**(n-place-1)
    if x < 0:
        num *= -1
    if num < -2**31 or num > 2**31 - 1:
        return 0
    return num

print(reverse_integer(123) == 321)
print(reverse_integer(-123) == -321)
print(reverse_integer(120) == 21)
print(reverse_integer(-2147483648) == 0)
print(reverse_integer(2147483647) == 0)
print(reverse_integer(0) == 0)
print(reverse_integer(1563847412) == 0)