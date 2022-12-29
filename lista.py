print("Program zapamiętuje ciągi znaków o nieparzystej długości")
a_list = []
while True:
    text = input("Podaj jakiś tekst, podaj pusty by zakończyć: ")
    if len(text) == 0:
        break
    if len(text) % 2 != 0:
        a_list.append(text)
if len(a_list):
    print("Podałeś następujące teksty o nieparzystej liczbie znaków:")
    for i in range(0, len(a_list)):
        print(f"{i+1}: {a_list[i]}")
else:
    print("Nie podałeś tekstów o nieparzystej liczbie znaków!")
