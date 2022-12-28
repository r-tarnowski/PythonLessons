a = int(input())
b = int(input())

if a > b:
    print(f"Nieprawidłowy zakres: {a} jest większe od {b}")
else:
    for i in range(a, b+1):
        if i % 7 == 0 and str(i) == str(i)[::-1]:
            print(f"Szukana liczba to: {i}.")
            break
