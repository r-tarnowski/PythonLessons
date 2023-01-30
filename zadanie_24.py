numbers = [int(number) for number in input().split()]
numbers_template = [int(number) for number in input().split()]

first_part = []
for template in numbers_template:
    for number in numbers:
        if number == template:
            first_part.append(template)

for number in first_part:
    numbers.remove(number)

sorted_numbers = first_part

numbers.sort()
for number in numbers:
    sorted_numbers.append(number)

for number in sorted_numbers:
    print(number, end=" ")




