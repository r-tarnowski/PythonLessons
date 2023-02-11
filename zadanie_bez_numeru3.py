from random import randint
numbers = [int(number) for number in input().split()]
line = []
for i in range(numbers[3]):
    for j in range(numbers[2]):
        line.append(randint(numbers[0], numbers[1]))
    print(line)
    line.clear()




