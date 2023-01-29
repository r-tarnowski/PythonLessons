# a = int(input())
# b = int(input())
# c = int(input())
# print(f"Średnia arytmetyczna podanych liczb wynosi: {(a+b+c)/3}")

# numbers = input().split()
# print(numbers)
# print(type(numbers))
# sum_of_numbers = 0
# for number in numbers:
#     sum_of_numbers += int(number)
# print(f"Średnia arytmetyczna podanych liczb wynosi: {sum_of_numbers/len(numbers)}")

numbers = [int(number) for number in input().split()]
print(f"Średnia arytmetyczna podanych liczb wynosi: {sum(numbers)/len(numbers)}")

