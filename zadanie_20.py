num_of_elements = int(input())

if num_of_elements < 2:
    print("Podano za mało danych, minimalna liczba to 2")
    exit(0)

list_of_elements = []
for i in range(num_of_elements):
    list_of_elements.append(input())

seconds_after_midnight = []
for element in list_of_elements:
    hours = int(element[:2])
    minutes = int(element[3:5])
    seconds = int(element[6:8])
    num_of_seconds = seconds + 60 * minutes + 3600 * hours
    seconds_after_midnight.append(num_of_seconds)

seconds_after_midnight.sort()
minimal_delta = seconds_after_midnight[0] + (24*3600 - seconds_after_midnight[-1])
for i in range(1, len(seconds_after_midnight)):
    delta = seconds_after_midnight[i] - seconds_after_midnight[i-1]
    if delta < minimal_delta:
        minimal_delta = delta

print(f"Najmniejsza różnica czasowa wynosi {minimal_delta}s.")

