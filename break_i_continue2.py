# a+b+c+d+e == 25
# a, b, c, d, e != 0, 3, 5
# a <= b <= c <= d <= e

how_many = 0
for a in range(1, 10):
    if a == 3 or a == 5:
        continue
    for b in range(a, 10):
        if b == 3 or b == 5:
            continue
        for c in range(b, 10):
            if c == 3 or c == 5:
                continue
            for d in range(c, 10):
                if d == 3 or d == 5:
                    continue
                for e in range(d, 10):
                    if e == 3 or e == 5:
                        continue
                    if a + b + c + d + e != 25:
                        continue
                    # if a <= b <= c <= d <= e:
                    print(f"({a}, {b}, {c}, {d}, {e})")
                    how_many += 1
print(f"Liczba kombinacji: {how_many}")
