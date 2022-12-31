lista = [55, 66, 77, 88, 99, 111]
print(lista)
for i in range(len(lista)):
    print(f"i: {i}, lista[ i ]: {lista[ i ]}")
for element in lista:
    print(f"kolejnym elementem listy jest: {element}")
for i, element in enumerate(lista):
    print(f"Elementem {i} listy jest: {element}")
    