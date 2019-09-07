"""Try to implement Fib problem using DP"""

memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    f = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = f
    return f

def fib_r(n):
    if n == 1 or n == 2:
        return 1
    return fib_r(n-1) + fib_r(n-2)


print("Recursive:", fib_r(14))
print("Memoized DP:", fib_memo(14))
