print(list(range(5)))
print(list(range(3, 15)))
print(list(range(3, 15, 2)))
print(list(range(3, 15, 3)))
print("--------------------------------------------")


def my_range(start=0, stop=10):
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += 1
    return result


print(my_range())
print(my_range(2))
print(my_range(2, 8))
print(my_range(stop=8))
print("--------------------------------------------")


def better_range(start, stop=None, step=1):
    result = []

    if stop:
        i = start
        while i < stop:
            result.append(i)
            i += step
    else:
        stop = start
        start = 0
        i = start
        while i < stop:
            result.append(i)
            i += step

    return result


# print(better_range())
print(better_range(5))
print(better_range(3, 15))
print(better_range(3, 15, 2))
print(better_range(3, 15, 3))
print("--------------------------------------------")


def refactored_range(start, stop=None, step=1):
    result = []

    if not stop:
        stop = start
        start = 0

    i = start
    while i < stop:
        result.append(i)
        i += step

    return result


# print(better_range())
print(refactored_range(5))
print(refactored_range(3, 15))
print(refactored_range(3, 15, 2))
print(refactored_range(3, 15, 3))
