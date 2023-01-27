my_list = [x**2 for x in range(-10, 10)]
print(my_list)
my_set = {x**2 for x in range(-10, 10)}
print(my_set)
# Ale UWAGA na tuple (obiekty niemodyfikowalne):
my_tuple = tuple(x**2 for x in range(-10, 10))
print(my_tuple)