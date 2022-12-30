numbers = []
sum_of_numbers = 0
counter = int(input())
for i in range(counter):
    number = int(input())
    if sum_of_numbers + number > 0:
        numbers.append(number)
        sum_of_numbers += number
print(f"Oto lista wpisanych przez Ciebie liczb (prócz krytycznych): {numbers}")
