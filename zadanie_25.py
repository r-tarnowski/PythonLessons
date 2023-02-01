text = input()
text_elements = {}
for character in text:
    if character.isalpha():
        value = text_elements.get(character, -1)
        if value == -1:
            text_elements[character] = 1
        else:
            value += 1
            text_elements[character] = value

text_elements_keys = list(text_elements.keys())
text_elements_values = list(text_elements.values())

for i in range(len(text_elements_keys)):
    print(f"{text_elements_keys[i]} - {text_elements_values[i]}")

