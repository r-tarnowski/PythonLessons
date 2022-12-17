for i in range(1, 11):
    for j in range(1, 11):
        # print(str(i*j).zfill(2), end=", ")
        result = i*j
        if len(str(result)) == 1:
            print(" ", end="")
        print(result, end=", ")
    print()
