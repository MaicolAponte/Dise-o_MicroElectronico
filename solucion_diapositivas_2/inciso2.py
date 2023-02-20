ancho = float(input('Ingrese el ancho del cultivo en pies: '))
largo = float(input('Ingrese la longitud del cultivo en pies: '))

area = ancho*largo
area_a = area/43560


print(f'El area del cultivo es de: {area_a:.2f} acres')