

def multiply_digits(input_number):
    result = 1
    for j in range(len(input_number)):
        result = result * int(input_number[j])
    return result


# input_val = input()
# print(f"Result for 333{input_val} is: {multiply_digits(input_val)}")

input_data = input().split(" ")
sum_of_multiplies = 0
for i in range( int(input_data[0]), int(input_data[1]) + 1):
    sum_of_multiplies += multiply_digits(str(i))
print(f"Suma iloczynów cyfr liczb od {input_data[0]} do {input_data[1]} wynosi: {sum_of_multiplies}.")

