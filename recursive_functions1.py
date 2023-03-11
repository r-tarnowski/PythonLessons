import sys
sys.setrecursionlimit(3000)


def foo(text):
    print(text)
    if text:
        foo(text[:-1])


# foo("Witam serdecznie!")


def factorial(n):
    if n <= 1:
        return 1
    rec_factorial = factorial(n-1)
    result = n * rec_factorial
    print(f"n = {n}, rec_factorial = {rec_factorial}, result = {result}")
    return result


def factorial2(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


factorial(5)
print(f"5! = {factorial2(5)}")

