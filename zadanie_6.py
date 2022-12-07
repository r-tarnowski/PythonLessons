x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("Punkt (0,0) znajduje się na obu osiach układu współrzędnych.")
elif x == 0:
    print("Punkt znajduje się na osi OY.")
elif y == 0:
    print("Punkt znajduje się na osi OX.")
else:
    quarta = "I/II/III/IV"
    if (x > 0) and (y > 0):
        quarta = "I"
    elif (x < 0) and (y > 0):
        quarta = "II"
    elif (x < 0) and (y < 0):
        quarta = "III"
    else:
        quarta = "IV"
    print(f"Punkt znajduje się w {quarta} ćwiartce układu współrzędnych.")
