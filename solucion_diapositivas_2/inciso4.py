letra = input('Ingrese una letra del alfabeto: ')

if letra in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
    print(f'La letra es una vocal.')
elif letra in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
               'ñ','p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
               'B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q'
               ,'R','S','T','V','W','X','Y','Z']:
    print(f'La letra es una consonate.')
else:
    print(f'Caracter no valido.')
       