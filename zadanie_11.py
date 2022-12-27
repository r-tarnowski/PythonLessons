still_number = True
counter = 0.0
sum_of_numbers = 0.0

while still_number:
    text = input()
    try:
        number = float(text)
    except ValueError:
        still_number = False
        continue
    sum_of_numbers += number
    counter += 1.0
print(f"Średnia arytmetyczna podanych przez Ciebie liczb wynosi: {sum_of_numbers/counter}.")
