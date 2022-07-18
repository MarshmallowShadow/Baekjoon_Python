def factorial(num):
    if num == 0:
        return 1
    recurse = num * factorial(num-1)
    return recurse


N = int(input())
print(factorial(N))


