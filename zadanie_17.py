x_min = 1
x_max = 8
y_min = 1
y_max = 8

plus_plus_flag = True
minus_minus_flag = True
minus_plus_flag = True
plus_minus_flag = True

position = input()
letter_indexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
digit_indexes = ['1', '2', '3', '4', '5', '6', '7', '8']
position_names = []

x_ = 1 + letter_indexes.index(position[0])
y_ = int(position[1])

# print(f"Start position: ({x_},{y_})")

# x_start = int(input())
# y_start = int(input())

x_start = x_
y_start = y_

if x_start == x_min:
    minus_plus_flag = False
    minus_minus_flag = False

if x_start == x_max:
    plus_plus_flag = False
    plus_minus_flag = False

if y_start == y_min:
    minus_minus_flag = False
    plus_minus_flag = False

if y_start == y_max:
    plus_plus_flag = False
    minus_plus_flag = False

# print(f"plus_plus_flag {plus_plus_flag}")
# print(f"minus_minus_flag {minus_minus_flag}")
# print(f"plus_minus_flag {plus_minus_flag}")
# print(f"minus_plus_flag {minus_plus_flag}")

counter = 0

if plus_plus_flag:
    x = x_start
    y = y_start
    while x < x_max and y < y_max:
        counter += 1
        x += 1
        y += 1
        position_name = letter_indexes[x-1]
        position_name += digit_indexes[y-1]
        position_names.append(position_name)


if minus_minus_flag:
    x = x_start
    y = y_start
    while x > x_min and y > y_min:
        counter += 1
        x -= 1
        y -= 1
        position_name = letter_indexes[x - 1]
        position_name += digit_indexes[y - 1]
        position_names.append(position_name)

if minus_plus_flag:
    x = x_start
    y = y_start
    while x > x_min and y < y_max:
        counter += 1
        x -= 1
        y += 1
        position_name = letter_indexes[x - 1]
        position_name += digit_indexes[y - 1]
        position_names.append(position_name)

if plus_minus_flag:
    x = x_start
    y = y_start
    while x < x_max and y > y_min:
        counter += 1
        x += 1
        y -= 1
        position_name = letter_indexes[x - 1]
        position_name += digit_indexes[y - 1]
        position_names.append(position_name)

for y in range(y_max):
    if (y + 1) != y_start:
        counter += 1
        position_name = letter_indexes[x_start - 1]
        position_name += digit_indexes[y]
        position_names.append(position_name)

for x in range(x_max):
    if (x + 1) != x_start:
        counter += 1
        position_name = letter_indexes[x]
        position_name += digit_indexes[y_start - 1]
        position_names.append(position_name)

# print(f"Hetman z tego miejsca może przejść na {counter} pól.")
# position_names.sort()
# print(position_names)
# for name in position_names:
#     print(name, end=", ")
# print()

position_names.sort()
for i in range(len(position_names)):
    if i == (len(position_names) - 1):
        print(position_names[i], end="")
    else:
        print(position_names[i], end=", ")
print()
