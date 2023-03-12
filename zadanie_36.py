def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True
    else:
        # print(f"text[0]: {text[0]}, text[-1]: {text[-1]}")
        if text[0] != text[-1]:
            return False
        else:
            return is_palindrome(text[1:-1])


input_text = input()
if is_palindrome(input_text):
    print("Podany tekst jest palindromem")
else:
    print("Podany tekst nie jest palindromem")

