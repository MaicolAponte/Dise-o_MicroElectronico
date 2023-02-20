def leer_archivo1():
    lista_num1 = []
    with open('Numeros del 0 al 100.txt', 'r') as f1:
        num = f1.readline()
        while num!="":
            lista_num1.append(int(num))
            num = f1.readline()
    f1.close()    
    return lista_num1 

        
def leer_archivo2():
    lista_num2 = []
    with open('Numeros del 50 al 200.txt', 'r') as f2:
        num = f2.readline()
        while num!="":
            lista_num2.append(int(num))
            num = f2.readline()
    f2.close()    
    return lista_num2


def organizar(lista):
    lista = sorted(lista, reverse = True)
    print(f'La lista de los numeros leidos de mayor a menor es:\n{lista}')


def eliminar_iguales(lista):
    for i in range(len(lista)-1,-1,-1):
        num = lista[i]
        for x in range(i-1,-1,-1):
            comparador = lista[x]
            if num == comparador:
                lista.pop(x)
    
    return lista
                   
                    
if __name__ == '__main__':
    lista_num1 = leer_archivo1()
    lista_num2 = leer_archivo2()
    lista = lista_num1 + lista_num2 
    lista = eliminar_iguales(lista)
    organizar(lista)
     

