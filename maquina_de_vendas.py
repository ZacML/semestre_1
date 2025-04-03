print('1- Miojo')
print('2- Misto')
print('3- Pizza')
print('4- Patel')
print('5- croissant')

num = int(input('Insira o numero correspondente ao prato desejado: '))

if num == 1:
    print('Macarrão instanâneo')
elif num == 2:
    print('Pão com presunto e queijo feito na chapa')
elif num == 3:
    print('Massa italiana com molho de tomate e peperoni')
elif num == 4:
    print('Massa de pastel com carne')
elif num == 5:
    print('Croissant recheado com chocolate')
else: 
    print('Número inválido')
