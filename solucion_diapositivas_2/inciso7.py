def organizar(lista):
    ordenados = sorted(lista)
    print(f'La lista de los numeros ingresados de menor a mayor es: {ordenados}')
    
    
    
def solicitud():
    lista = []
    sol = True
    while sol:
        num = int(input('Ingrese un numero, si ingresa "0" dejara de ingresar numeros: '))
        if num == 0:
            break
        else:
            lista.append(num)
            
    organizar(lista)
            
            
if __name__ == '__main__':
    solicitud()