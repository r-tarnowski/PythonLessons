list2d = [[1, 2, 3], ["a", "b", "c"], [True, False, True]]
print(f"list2d: {list2d}")
print(f"list2d[0]: {list2d[0]}")
print(f"list2d[1]: {list2d[1]}")
print(f"list2d[2]: {list2d[2]}")
print(f"list2d[1][1]: {list2d[1][1]}")
print()
list3d = [[1, 2, 3], ["a", "b", "c"], [True, [6, 9, 12], True]]
print(f"list3d: {list3d}")
print(f"list3d[0]: {list3d[0]}")
print(f"list3d[1]: {list3d[1]}")
print(f"list3d[2]: {list3d[2]}")
print(f"list3d[1][1]: {list3d[1][1]}")
print(f"list3d[2][1]: {list3d[2][1]}")
print(f"list3d[2][1][2]: {list3d[2][1][2]}")
print("UWAGA: indeks -1 oznacza ostatni element z listy, dlatego:")
print(f"list3d[-1][1][-1]: {list3d[-1][1][-1]}")
print()
chessboard = [
    ["w", "s", "g", "h", "k", "g", "s", "w"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["@", "@", "@", "@", "@", "@", "@", "@"],
    ["@", "@", "@", "@", "@", "@", "@", "@"],
    ["@", "@", "@", "@", "@", "@", "@", "@"],
    ["@", "@", "@", "@", "@", "@", "@", "@"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["W", "W", "G", "H", "K", "G", "S", "W"]
]

for element in chessboard:
    print(element)

print()
for line in chessboard:
    for element in line:
        print(element, end=" ")
    print()

print()
for line in chessboard:
    print("-".join(line))

print()
for line in chessboard:
    print(" ".join(line))

print()
for i in range(len(chessboard)):
    for j in range(len(chessboard[i])):
        print(chessboard[i][j], end=" ")
    print()

print()
for line in chessboard:
    print(line[4], end=", ")
