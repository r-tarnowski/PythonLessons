def calc_an(num_of_steps, start_val):
    for i in range(num_of_steps):
        an = start_val*start_val - 2*start_val
        print(an)
        start_val = an


input_data = input().split(" ")
# print(input_data)
n = int(input_data[0])
a1 = int(input_data[1])
calc_an(n, a1)
# print(f"n = {n}, a1 = {a1}")


