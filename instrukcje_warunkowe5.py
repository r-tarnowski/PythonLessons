number = int(input("Podaj liczbę z zakresu 1-99999: "))
if number < 0:
    print("Podałeś liczbę spoza zakresu")
elif number < 10:
    print("Podałeś liczbę jednocyfrową")
elif number < 100:
    print("Podałeś liczbę dwucyfrową")
elif number < 1000:
    print("Podałeś liczbę trzycyfrową")
elif number < 10000:
    print("Podałeś liczbę czterocyfrową")
elif number < 100000:
    print("Podałeś liczbę pięciocyfrową")
else:
    print("Podałeś liczbę spoza zakresu")

