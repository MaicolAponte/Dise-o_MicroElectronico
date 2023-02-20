def solicitud():
    lista = []
    sol = True
    
    while sol:
        palabra = input('Ingrese una palabra, si ingresa "fin" dejara de ingresar palabras: ')
        if palabra == 'fin':
            break
        else:
            if palabra in lista:
                pass
            else:
                lista.append(palabra)
            
    print(f'La lista de palabras es: {lista}')
    
            
if __name__ == '__main__':
    solicitud()
        
        