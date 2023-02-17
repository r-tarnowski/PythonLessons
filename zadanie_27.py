patterns_text = input().lower()
text_to_check = input()

patterns = patterns_text.split()

text_items = []
alpha_item = ""
for k in range(len(text_to_check)):
    if text_to_check[k].isalpha():
        alpha_item = alpha_item + text_to_check[k]
    else:
        if len(alpha_item) > 0:
            text_items.append(alpha_item)
            alpha_item = ""
        text_items.append(text_to_check[k])

if len(alpha_item) > 0:
    text_items.append(alpha_item)

censored_flag = False
for pattern in patterns:
    for i in range(len(text_items)):
        if text_items[i].lower() == pattern:
            censored_flag = True
            new_item = text_items[i][0]
            for j in range(1, len(text_items[i])):
                new_item = new_item + "*"
            text_items[i] = new_item

output_text = ""
for item in text_items:
    output_text = output_text + item

print(output_text)
if censored_flag:
    print("Tekst został ocenzurowany!")
