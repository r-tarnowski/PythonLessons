text = input()

text = text.strip()
text = text.rstrip()

words = []
word = []
for i in range(len(text)):
    if text[i].isalpha():
        word.append(text[i])
        if i == len(text) - 1:
            word.reverse()
            words.append(word)
            word = []
    else:
        word.reverse()
        if text[i] != " ":
            word.append(text[i])
        if len(word) > 0:
            words.append(word)
            word = []

for j in range(len(words)):
    for i in range(len(words[j])):
        print(words[j][i], end="")
    if j != len(words) - 1:
        print(" ", end="")

print()
