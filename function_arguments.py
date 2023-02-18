

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
        print("".join(new_coll))
    else:
        print(new_coll)


numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']
merge_two_collections_alternately(numbers, letters)
merge_two_collections_alternately(letters, numbers)

text1 = "kot"
text2 = "123"
merge_two_collections_alternately(text1, text2)
merge_two_collections_alternately(text2, text1)

