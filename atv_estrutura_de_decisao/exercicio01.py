nm1 = int(input('Insira um número inteiro: '))
nm2 = int(input('Insira um número inteiro: '))
nm3 = int(input('Insira um número inteiro: '))

if nm1 > nm2 and nm1 > nm3:
    print('O primeiro número digitado é maior')
elif nm2 > nm1 and nm2 > nm3:
    print('O segundo número digitado é maior')
elif nm3 > nm1 and nm3 > nm2:
    print('O terceiro número digitado é maior')
