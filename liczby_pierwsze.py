primes = [2]
to_check = 3
while len(primes) < 1001:
    is_prime = True
    for i in range(2, to_check):
        if to_check % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(to_check)
    to_check += 2
print(primes)
