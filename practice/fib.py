"""Try to implement Fib problem using DP"""

def fib_r(n):
    if n == 1 or n == 2:
        return 1
    return fib_r(n-1) + fib_r(n-2)

memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    f = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = f
    return f

fib = {}
def fib_bottom_up(n):
    for k in range(1, n + 1):
        if k <= 2:
            fib[k] = 1
        else:
            fib[k] = fib_bottom_up(k -1) + fib_bottom_up(k - 2)
    return fib[n]

print("Recursive:", fib_r(14))
print("Memoized DP:", fib_memo(14))
print("Bottom Up DP:", fib_bottom_up(14))