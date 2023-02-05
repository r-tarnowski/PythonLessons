alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

mapping = {}
for index, letter in enumerate(alphabet, 1):
    mapping[index] = letter

text = input()
input_code = text.split(",")

decoded_text = ""
for code in input_code:
    decoded_text = decoded_text + mapping[int(code)]

print(decoded_text)


