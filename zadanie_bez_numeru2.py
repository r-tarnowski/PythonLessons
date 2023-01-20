from random import randint

numbers = []
while len(numbers) < 6:
    number = randint(1, 49)
    if number in numbers:
        pass
    else:
        numbers.append(number)

for i in range(len(numbers)):
    if i < (len(numbers) - 1):
        print(numbers[i], end=", ")
    else:
        print(numbers[i])

