simple_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 1, 2, 3, 10}
simple_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 1, 2, 3, 10]
print(simple_set)
print(simple_list)
unique_list = list(set(simple_list))
print(unique_list)
set1 = {1, 2, 3, 4, 5, '1', '2', '3', '4', '5', True, 3.5, "ala", 'x', ' '}
list1 = [1, 2, 3, 4, 5, '1', '2', '3', '4', '5', True, 3.5, "ala", 'x', ' ']
print(f"set1: {set1}")
print(list1)

for element in set1:
    print(element, end=", ")
print()

set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"set2: {set2}")
print(f"iloczyn set1 & set2: {set1 & set2}")
print(f"suma set1 | set2: {set1 | set2}")

set2.add('6')
print(f"set2 po dodaniu '6': {set2}")




