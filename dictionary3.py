alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
alphabet += alphabet.upper();
print(alphabet)

mapping = {}
for index, letter in enumerate(alphabet, 1):
    mapping[letter] = index
print(mapping)

mapping2 = {letter: index for index, letter in enumerate(alphabet, 1)}
print(mapping2)

mapping.pop('a')
print(mapping)

list_of_keys = list(mapping.keys())
print(list_of_keys)

list_of_values = list(mapping.values())
print(list_of_values)

for key, value in mapping2.items():
    if value % 2 == 0 and key.islower():
        print(f"{key}: {value}")

print(len(mapping2))

dict1 = {'a': 1}
dict2 = {'b': 2}
print(dict1 | dict2)
dict1 |= dict2
print(dict1)
