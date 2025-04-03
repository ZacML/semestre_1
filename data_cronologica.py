dia1 = int(input('Insira o dia da primeira data: '))
mes1 = int(input('Insira o mes da primeira data: '))
ano1 = int(input('Insira o ano da primeira data: '))

dia2 = int(input('Insira o dia da segunda data: '))
mes2 = int(input('Insira o mes da segunda data: '))
ano2 = int(input('Insira o ano da segunda data: '))

if ano1 < ano2 or (ano1 == ano2 and mes1 < mes2) or (ano1 == ano2 and mes1 == mes2 and dia1 < dia2):
    print('A primeira data ocorreu cronologicamente primeiro.')
elif ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
    print('As duas datas inseridas são iguais.')
else:
    print("A segunda data ocorreu cronologicamente primeiro.")
