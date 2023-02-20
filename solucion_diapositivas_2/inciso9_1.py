def esc_archivo1():
    with open('Numeros del 0 al 100.txt', 'w') as f1:
        for i in range(0,101):
            f1.write('{i}'.format(i = i))
            f1.write('\n')
    f1.close()
            
            
def esc_archivo2():
    with open('Numeros del 50 al 200.txt', 'w') as f2:
       for j in range(50,201):
            f2.write('{j}'.format(j = j))
            f2.write('\n')
    f2.close()        

if __name__ == '__main__':
    esc_archivo1()
    esc_archivo2()