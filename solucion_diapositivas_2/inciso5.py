def archivo(fila,titulo):
    if titulo == 1:
        with open('MATRIX.txt', 'w') as f:
            f.write('                            MATRIX DE COMBINACIONES PARA LA MULTIPLICACION DE NUMEROS DEL 1 AL 10\n\n')
            titulo = 0
    else:
        with open('MATRIX.txt', 'a') as f:
            f.write('{tabla1:>7}  {tabla2:>10}  {tabla3:>10}  {tabla4:>10}  {tabla5:>10}  {tabla6:>10}  {tabla7:>10}  {tabla8:>10}  {tabla9:>10}  {tabla10:>10}\n'.format(
                tabla1=fila[0], tabla2=fila[1], tabla3=fila[2], tabla4=fila[3], tabla5=fila[4], tabla6=fila[5], tabla7=fila[6], tabla8=fila[7], tabla9=fila[8], tabla10=fila[9]))
    return titulo


def generar_matrix():
    # j * i  = result
    titulo = 1
    for i in range(0,11):
        fila = []
        for j in range(1,11):
            palabra = str(j) +'*'+ str(i)+ '=' +str(i*j)
            fila.append(palabra)

        titulo = archivo(fila, titulo)
 
            
if __name__ == '__main__':
    generar_matrix()