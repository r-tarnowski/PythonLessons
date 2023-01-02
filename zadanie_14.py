number = int(input())
elements = []
if number <= 0 or number > 1000000000:
    print("Podałeś liczbę spoza dopuszczalnego zakresu")
else:
    element = number
    elements.append(element)
    while element > 1:
        if element % 2 == 0:
            element //= 2
        else:
            element = 3 * element + 1
        elements.append(element)
print(f"Ciąg Collatza dla liczby startowej {number}: {elements}")

