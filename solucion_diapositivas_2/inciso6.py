def medio(list):
    ordenados = sorted(list, reverse = True)
    return ordenados[1]


def solicitud():
    numero = []
    for i in range(3):
        n = int(input('Ingrese un numero '))
        numero.append(n)
    
    vmedio = medio(numero)
    
    print(f'El valor medio de los numeros {numero[0]}, {numero[1]}, {numero[2]} es: {vmedio}')
    
    
if __name__ == '__main__':
    solicitud()

    
    