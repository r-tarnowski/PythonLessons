
def merge_two_collections_alternately(coll1, coll2):
    new_coll = []
    minimal_length = min(len(coll1), len(coll2))
    for i in range(minimal_length):
        if isinstance(coll1, list):
            new_coll.append(coll1[i])
            new_coll.append(coll2[i])
        else:
            new_coll += coll1[i]
            new_coll += coll2[i]

    if isinstance(coll1, str):
        return "".join(new_coll)
    else:
        return new_coll


def f(x):
    return 3*x**2 + 5*x +2


numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']
my_collection = merge_two_collections_alternately(numbers, letters)
print(f"my_collection: {my_collection}")
my_collection = merge_two_collections_alternately(letters, numbers)
print(f"my_collection: {my_collection}")

text1 = "kot"
text2 = "123"
my_collection = merge_two_collections_alternately(text1, text2)
print(f"my_collection: {my_collection}")
my_collection = merge_two_collections_alternately(text2, text1)
print(f"my_collection: {my_collection}")

print(f"f(3): {f(3)}")
print(f"f(5): {f(5)}")
print(f"f(0): {f(0)}")
