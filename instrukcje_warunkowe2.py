number = int(input("Podaj liczbę naturalną jednocyfrową: "))
if number < 0:
    print("Chcieliśmy liczbę dodatnią!")
else:
    if number > 9:
        print("Liczba miała być jednocyfrowa!")
    else:
        print("Podałeś poprawną liczbę. Dziękuję!")
