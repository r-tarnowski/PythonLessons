a = int(input())
b = int(input())

summary = 0
multip = 1

if a <= b:
    for i in range(a, b+1):
        summary += i
        multip *= i
    print(f"Suma twoich liczb wynosi: {summary}")
    print(f"Iloczyn twoich liczb wynosi: {multip}")
else:
    print("Początek przedziału musi być mniejszy bądź równy niż jego koniec!")
