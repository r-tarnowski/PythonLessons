def calc_an_rec(num_of_steps, start_val):
    if num_of_steps <= 1:
        an = start_val*start_val - 2*start_val
        # print(f"num_of_steps = {num_of_steps},  an = {an}")
        print(an)
        return an

    # print(f"num_of_steps = {num_of_steps}")
    an_1 = calc_an_rec(num_of_steps - 1, start_val)
    an = an_1*an_1 - 2*an_1
    # print(f"num_of_steps = {num_of_steps},  an_1 = {an_1}, an = {an}")
    print(an)
    return an


input_data = input().split(" ")
# print(input_data)
n = int(input_data[0])
a1 = int(input_data[1])
calc_an_rec(n, a1)
