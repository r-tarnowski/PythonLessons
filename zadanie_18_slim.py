
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
        line.append(0)
        values.append(value)
        value += 1
    a_matrix.append(line)

segments = []
segment_len = 1
value_index = len(values) - 1

while True:
    segment = []
    for i in range(segment_len):
        segment.append(values[value_index])
        value_index -= 1
    segment.reverse()
    segments.append(segment)

    if segment_len == n:
        break

    segment = []
    for i in range(segment_len):
        segment.append(values[value_index])
        value_index -= 1
    segment.reverse()
    segments.append(segment)

    segment_len += 1

segments.reverse()
num_of_steps = len(segments)
step_number = 0
steps_right = 0
steps_down = 0
steps_left = 0
steps_up = 0

while True:
    for i in range(len(segments[step_number])):
        a_matrix[steps_right][i + steps_up] = segments[step_number][i]
    steps_right += 1
    step_number += 1
    if step_number >= num_of_steps:
        break

    for i in range(len(segments[step_number])):
        a_matrix[steps_right + i][n - 1 - steps_down] = segments[step_number][i]
    steps_down += 1
    step_number += 1
    if step_number >= num_of_steps:
        break

    for i in range(len(segments[step_number])):
        a_matrix[n - 1 - steps_left][n - 1 - steps_down - i] = segments[step_number][i]
    steps_left += 1
    step_number += 1
    if step_number >= num_of_steps:
        break

    for i in range(len(segments[step_number])):
        a_matrix[n - 1 - steps_left - i][steps_up] = segments[step_number][i]
    steps_up += 1
    step_number += 1
    if step_number >= num_of_steps:
        break

for i in range(n):
    for j in range(n):
        if i == (n-1) and j == (n-1):
            print(a_matrix[i][j])
        else:
            print(a_matrix[i][j], end=", ")

