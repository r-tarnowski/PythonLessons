from random import choice, choices, sample, shuffle

a_list = [1, 10, 15, 2, 4]
print(f"a_list: {a_list}")
print(f"max(a_list) = {max(a_list)}")
print(f"min(a_list) = {min(a_list)}")
print(f"sum(a_list) = {sum(a_list)}")
print(f"sorted(a_list): {sorted(a_list)}")
print(f"UWAGA! a_list: {a_list}")
print(f"a_list.sort(): {a_list.sort()}")
print(f"UWAGA! a_list: {a_list}")
print("Iteracja po reversed(a_list)")
for element in reversed(a_list):
    print(element)

b_list = ['a', 'b', 'x', 'y', 'z']
print(f"b_list: {b_list}")
print("Iteracja po zip(a_list, b_list)")
for item in zip(a_list, b_list):
    print(item)

print(f"choice(a_list): {choice(a_list)}")
print(f"choice(a_list): {choice(a_list)}")
print(f"choice(a_list): {choice(a_list)}")
print(f"choices(a_list): {choices(a_list)}")
print(f"choices(a_list, k=2): {choices(a_list, k=2)}")
print(f"choices(a_list, k=3): {choices(a_list, k=3)}")
print(f"sample(a_list, k=1): {sample(a_list, k=1)}")
print(f"sample(a_list, k=2): {sample(a_list, k=2)}")
print(f"sample(a_list, k=3): {sample(a_list, k=3)}")
shuffle(a_list)
print(f"a_list after shuffle(a_list): {a_list}")
shuffle(a_list)
print(f"a_list after shuffle(a_list): {a_list}")
shuffle(a_list)
print(f"a_list after shuffle(a_list): {a_list}")

print("totolotek:")
possible_numbers = [x for x in range(1, 49+1)]
print(sample(possible_numbers, k=6))

