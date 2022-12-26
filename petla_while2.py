from random import randint

random_number = randint(1, 100)
user_number = int(input("Wylosowałem liczbę od 1 do 1000, spróbuj ją zgadnąć: "))
i = 1
while user_number != random_number:
    if user_number > random_number:
        print("Moja liczba jest mniejsza")
    else:
        print("Moja liczba jest większa")
    user_number = int(input("Spróbuj ponownie: "))
    i += 1
print(f"Zgadłeś za {i} razem, brawo!")
