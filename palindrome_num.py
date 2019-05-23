# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?
import math
def palindrome_num(num):
    if num < 0:
        return False
    elif num < 10:
        return True
    n = int(math.log(num, 10)) + 1 # number of digits
    stack = []
    for idx in range(n//2):
        digit = num // 10**idx % 10
        stack.append(digit)
    startIdx = n//2
    if n % 2 != 0:
        startIdx = n//2 + 1
    for idx in range(startIdx, n):
        digit = num // 10**idx % 10
        if stack.pop() != digit:
            return False
    return True
    





print(palindrome_num(120) == False)
print(palindrome_num(1) == True)
print(palindrome_num(9) == True)
print(palindrome_num(12) == False)
print(palindrome_num(245929542) == True)
print(palindrome_num(24592954) == False)
print(palindrome_num(2459229542) == True)


