text = input()
for i in range(len(text)):
    for j in range(len(text) - i):
        print(text[j], end="")
    print()

