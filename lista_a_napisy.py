text = "Ala ma kota"
a_list = ['A', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a']

print(text[0])
print(a_list[0])

print(len(text))
print(len(a_list))

text += '.'
print(text)

a_list += ['.']
print(a_list)

print(id(text))
print(id(text.upper()))
print(text)
another_text = text.upper()
print(another_text)
print(id(another_text))

print(a_list)
print(id(a_list))
a_list.append(" Dalsza część napisu")
print(a_list)
print(id(a_list))

print("================================================")
print(text)
b_list = list(text)
print(b_list)
b_list.sort()
print(b_list)

b_text = "".join(b_list)
print(b_text)

b_text = "<>".join(b_list)
print(b_text)


