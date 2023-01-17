# a+b+c+d+e == 25
# a, b, c, d, e != 0, 3, 5
# a <= b <= c <= d <= e

how_many = 0
for i in range(10000, 99999+1):

    i_as_text = str(i)
    if '0' in i_as_text or '5' in i_as_text or '3' in i_as_text:
        continue

    i_as_list1 = list(i_as_text)
    i_as_list2 = list(i_as_text)
    i_as_list2.sort()
    if i_as_list1 != i_as_list2:
        continue

    summary = 0
    for char in i_as_list2:
        summary += int(char)
    if summary != 25:
        continue

    print(i)
    how_many += 1

print(f"Liczba kombinacji: {how_many}")