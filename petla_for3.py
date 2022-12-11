result = 0;
for i in range(1001):
    if i % 3 == 0 and str(i) == str(i)[::-1]:
        result += i
print(f"Suma liczb z zakresu od 0 do 1000 podzielnych przez 3 będących jednocześnie palindromami wynosi: {result}")