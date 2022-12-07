a = float(input("Podaj współczynnik 'a' funkcji kwadratowej: "))
b = float(input("Podaj współczynnik 'b' funkcji kwadratowej: "))
c = float(input("Podaj współczynnik 'c' funkcji kwadratowej: "))
delta = b**2 - 4*a*c
if delta > 0:
    print("Ta funkcja kwadratowa ma dwa pierwiastki")
elif delta == 0:
    print("Ta funkcja kwadratowa ma jeden podwójny pierwiastek")
else:
    print("Ta funkcja kwadratowa nie ma pierwiastków")
