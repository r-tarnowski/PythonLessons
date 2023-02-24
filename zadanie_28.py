

def merge_three_collections_alternately(coll1, coll2, coll3):
    new_coll = []
    minimal_length = min(len(coll1), len(coll2), len(coll3))
    for i in range(minimal_length):
        if isinstance(coll1, list):
            new_coll.append(coll1[i])
            new_coll.append(coll2[i])
            new_coll.append(coll3[i])
        else:
            new_coll += coll1[i]
            new_coll += coll2[i]
            new_coll += coll3[i]

    if isinstance(coll1, str):
        print("".join(new_coll))
    else:
        print(new_coll)


text1 = input()
text2 = input()
text3 = input()
merge_three_collections_alternately(text1, text2, text3)
