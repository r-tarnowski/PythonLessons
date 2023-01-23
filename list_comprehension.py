numbers = []
text = "1234"
for char in text:
    numbers.append(int(char))
print(numbers)

# [CO Z TYM ZROBIĆ for CO in PO CZYM]
numbers = [int(char) for char in text]
print(numbers)

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square_numbers = []
for number in some_list:
    square_numbers.append(number**2)
print(square_numbers)

square_numbers = []
for number in range(1, 10):
    square_numbers.append(number**2)
print(square_numbers)

square_numbers = [number**2 for number in some_list]
print(square_numbers)

square_numbers = [number**2 for number in range(1, 10)]
print(square_numbers)

square_some_numbers = []
for number in range(1, 16):
    if '3' not in str(number) and '5' not in str(number):
        square_some_numbers.append(number**2)
print(square_some_numbers)

# [CO Z TYM ZROBIĆ for CO in PO CZYM PRZY JAKIM WARUNKU]
square_some_numbers = [number**2 for number in range(1, 17) if '3' not in str(number) and '5' not in str(number)]
print(square_some_numbers)

