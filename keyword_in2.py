a_list = [5, 10, 15, 20, True, "Prawda", False]
text = "Dowolny tekst"
print(f"text: {text}")
if "w" in text:
    print("Litera 'w' występuje w tekście")
else:
    print("Litera 'w' nie występuje w tekście")

print(f"a_list: {a_list}")
if "w" in a_list:
    print("Tekst 'w' występuje w liście")
else:
    print("Tekst 'w' nie występuje w liście")

a_list.append("w")

print(f"a_list: {a_list}")
if "w" in a_list:
    print("Tekst 'w' występuje w liście")
else:
    print("Tekst 'w' nie występuje w liście")

n = 3
if n in a_list:
    print(f"Liczba {n} występuje w liście")
else:
    print(f"Liczba {n} nie występuje w liście")

n = 5
if n in a_list:
    print(f"Liczba {n} występuje w liście")
else:
    print(f"Liczba {n} nie występuje w liście")

x = 5
y = 20
if x in a_list and y in a_list:
    index_of_x = a_list.index(x)
    index_of_y = a_list.index(y)
    if abs(index_of_y - index_of_x) == 1:
        print(f"Liczby {x} i {y} znajdują się obok siebie")
    else:
        print(f"Liczby {x} i {y} nie znajdują się obok siebie")
else:
    print(f"Liczba {x} lub liczba {y} nie występuje w liście: {a_list}")