for i in range(1, 1000):
    print(i)
    if i % 7 == 0 and i % 51 == 0:
        print(f"Znalazłem, jest to: {i}")
        break
        