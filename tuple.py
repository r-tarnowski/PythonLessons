a_list = [1, 2, 3, 4]
a_tuple = (1, 2, 3, 4)
print(a_tuple, a_list)
print(a_tuple[1], a_list[1])

tuple2d = ((1, 2, 3), ("a", "b", "c"), (True, [6, 9, 12], True))
print(tuple2d)
print(tuple2d[-1][1][-1])
print( "Tuple są niemodyfikowalne, ale można zmodyfikować listę, która jest elementem tupli:")
tuple2d[-1][1][-1] = 11
print(tuple2d)
print(tuple2d[-1][1][-1])

print(id(a_list))
a_list.append(5)
print(a_list)
print(id(a_list))

print(id(a_tuple))
a_tuple += (6, )
print(a_tuple)
print(id(a_tuple))

