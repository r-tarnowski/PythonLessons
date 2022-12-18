n = int(input())
if n > 0:
    hash_flag = True
    first_hash_flag = True
    for i in range(n):
        for j in range(n):
            if hash_flag:
                print("#", end="")
                hash_flag = False
            else:
                print("@", end="")
                hash_flag = True
        print()
        if first_hash_flag:
            first_hash_flag = False
            hash_flag = False
        else:
            first_hash_flag = True
            hash_flag = True
else:
    print("Liczba musi być większa od zera")
