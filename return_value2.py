def foo(x):
    pass


def bar(x):
    print(1)
    print(2)
    return 2*x


def celsius2kelvin(temperature):
    if temperature < -273.15:
        return
    return temperature + 273.15


def bar2(x):
    return 2*x, 3*x, 4*x


print(foo(3))
print(bar(3))
print(celsius2kelvin(100))
print(celsius2kelvin(-300))
a, b, c = bar2(2)
print(a, b, c)
print(f"ATTENTION! type(bar2(2)) is {type(bar2(2))}, not three independent objects.")
