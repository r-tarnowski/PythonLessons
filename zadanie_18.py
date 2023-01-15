# matrix = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10],
#           [11, 12, 13, 14, 15],
#           [16, 17, 18, 19, 20],
#           [21, 22, 23, 24, 25]]

# print(matrix[1][1])
# print(matrix[4][3])

n = int(input())
if n <= 0:
    print("Podałeś liczbę spoza zakresu")
    exit(0)

if n == 1:
    print("1")
    exit(0)

value = 1
a_matrix = []
values = []
for row in range(n):
    line = []
    for i in range(n):
        # line.append(value)
        line.append(0)
        values.append(value)
        value += 1
    a_matrix.append(line)

# segment = []
segments = []
# reverse_segment = []
reverse_segments = []
segment_len = 1
value_index = len(values) - 1

while True:
    segment = []
    reverse_segment = []
    for i in range(segment_len):
        print(f"value_index = {value_index}")
        print(f"values[value_index] = {values[value_index]}")
        segment.append(values[value_index])
        value_index -= 1
    segments.append(segment)
    reverse_segment = segment.copy()
    reverse_segment.reverse()
    reverse_segments.append(reverse_segment)
    print(f"segment = {segment}")
    print(f"segments = {segments}")
    print(f"reverse_segment = {reverse_segment}")
    print(f"reverse_segments = {reverse_segments}")

    if segment_len == n:
        break

    segment = []
    reverse_segment = []
    for i in range(segment_len):
        print(f"value_index = {value_index}")
        print(f"values[value_index] = {values[value_index]}")
        segment.append(values[value_index])
        value_index -= 1
    segments.append(segment)
    reverse_segment = segment.copy()
    reverse_segment.reverse()
    reverse_segments.append(reverse_segment)
    print(f"segment = {segment}")
    print(f"segments = {segments}")
    print(f"reverse_segment = {reverse_segment}")
    print(f"reverse_segments = {reverse_segments}")

    segment_len += 1

print(f"Macierz: {a_matrix}")
print(f"Wszystkie wartości: {values}")
values_reverse = values.copy()
values_reverse.reverse()
print(f"Wszystkie wartości w odwrotnej kolejności: {values_reverse}")
print(f"Wszystkie wartości raz jeszcze: {values}")
print(f"Segmenty: {segments}")
print(f"Segmenty odwrócone: {reverse_segments}")
reverse_reverse_segments = reverse_segments.copy()
reverse_reverse_segments.reverse()
print(f"Odwrócone segmenty odwrócone: {reverse_reverse_segments}")

num_of_steps = len(reverse_reverse_segments)
print(f"num_of_steps = {num_of_steps}")
step_number = 0
steps_right = 0
steps_down = 0
steps_left = 0
steps_up = 0

while True:
    for i in range(len(reverse_reverse_segments[step_number])):
        a_matrix[steps_right][i + steps_up] = reverse_reverse_segments[step_number][i]
    steps_right += 1
    step_number += 1
    if step_number >= num_of_steps:
        break

    for i in range(len(reverse_reverse_segments[step_number])):
        a_matrix[steps_right + i][n - 1 - steps_down] = reverse_reverse_segments[step_number][i]
    steps_down += 1
    step_number += 1
    if step_number >= num_of_steps:
        break

    for i in range(len(reverse_reverse_segments[step_number])):
        a_matrix[n - 1 - steps_left][n - 1 - steps_down - i] = reverse_reverse_segments[step_number][i]
    steps_left += 1
    step_number += 1
    if step_number >= num_of_steps:
        break


    for i in range(len(reverse_reverse_segments[step_number])):
        a_matrix[n - 1 - steps_left - i][steps_up] = reverse_reverse_segments[step_number][i]
    steps_up += 1
    step_number += 1
    if step_number >= num_of_steps:
        break


print(f"Macierz: {a_matrix}")

