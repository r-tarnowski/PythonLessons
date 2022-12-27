squares = []
user_number = 1
while user_number != 0:
    user_number = int(input())
    if user_number:
        square = [user_number * user_number]
        squares += square
for result in squares:
    print(f"Kwadrat Twojej liczby wynosi: {result}")
