import math

variable = float(input())
if variable < 0.0:
    print("Nie można pierwiastkować liczby ujemnej pierwiastkiem stopnia parzystego!")
else:
    print(f"Pierwiastek Twojej liczby wynosi: {math.sqrt(variable)}")
