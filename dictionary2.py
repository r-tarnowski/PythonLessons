amount_to_name = {
    2: 'dwóch',
    3: 'trzech',
    4: 'czterech',
    5: 'pięciu',
    6: 'sześciu',
    7: 'siedmiu',
    8: 'ośmiu',
    9: 'dziewięciu',
    10: 'dziesięciu'
}

numbers = [int(number) for number in input().split()]
if len(numbers) == 1:
    print(f"Średnia arytmeryczna hednej liczby wynosi: {numbers[0]}")
else:
    text = amount_to_name.get(len(numbers), len(numbers))
print(f"Średnia arytmetyczna podanych {text} liczb wynosi: {sum(numbers)/len(numbers)}")