

def check_bmi(height, weight):
    bmi = weight / (height * height)
    if bmi < 16.0:
        print("wygłodzenie")
    elif 16.0 <= bmi < 17.0:
        print("wychudzenie")
    elif 17 <= bmi < 18.5:
        print("niedowaga")
    elif 18.5 <= bmi < 25.0:
        print("pożądana masa ciała")
    elif 25.0 <= bmi < 30.0:
        print("nadwaga")
    elif 30.0 <= bmi < 35.0:
        print("otyłość I stopnia")
    elif 35.0 <= bmi < 40.0:
        print("otyłość II stopnia")
    else:
        print("otyłość III stopnia")


input_data = input().split(",")
if len(input_data) != 2:
    print("Niepoprawne dane wejściowe")
else:
    input_weight = float(input_data[0])
    input_height = float(input_data[1])
    check_bmi(input_height, input_weight)
