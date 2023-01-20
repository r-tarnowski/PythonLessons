template = input()
target = input()

template_list = list(template)
target_list = list(target)

allInTarget = True
for i in range(len(template_list)):
    if not template_list[i] in target_list:
        allInTarget = False
        break

if allInTarget:
    print(f"Wszystkie litery wyrazu {template} występują w wyrazie {target}.")
else:
    print(f"Nie wszystkie litery wyrazu {template} występują w wyrazie {target}.")
