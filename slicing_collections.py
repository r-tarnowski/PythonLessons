a_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
text = "Dowolny tekst"

print(a_list)
print(a_list[1])
print(a_list[1:4])

b_list = a_list[2:5]
print(b_list)
print(f"a_list id: {id(a_list)}")
print(f"b_list id: {id(b_list)}")
print(a_list[1:])
print(a_list[:5])
print(a_list[:])

print(text[1:4])

print(a_list[2:9:2])
print(a_list[::2])

print(a_list[-1:4])
print(a_list[-1:4:-1])
print(a_list[::-1])
print(text[::-1])

my_slice = slice(-1, 4, -1)
print(text[-1:4:-1])
print(text[my_slice])
print(a_list[-1:4:-1])
print(a_list[my_slice])





