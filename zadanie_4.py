val1 = float(input())
val2 = float(input())
val3 = float(input())

if val1 < val2 < val3:
    print(f"{val1} < {val2} < {val3}")
else:
    if val1 > val2 > val3:
        print(f"{val1} > {val2} > {val3}")
    else:
        print("Liczby nie tworzą ciągu rosnącego/malejącego.")
