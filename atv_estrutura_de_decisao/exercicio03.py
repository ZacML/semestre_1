dia1 = int(input('Insira o dia da primeira data: '))
mes1 = int(input('Insira o mes da primeira data: '))
ano1 = int(input('Insira o ano da primeira data: '))

dia2 = int(input('Insira o dia da segunda data: '))
mes2 = int(input('Insira o mes da segunda data: '))
ano2 = int(input('Insira o ano da segunda data: '))

#meu jeito
if ano1 < ano2 or (ano1 == ano2 and mes1 < mes2) or (ano1 == ano2 and mes1 == mes2 and dia1 < dia2):
    print('A primeira data ocorreu cronologicamente primeiro.')
elif ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
    print('As duas datas inseridas são iguais.')
else:
   print("A segunda data ocorreu cronologicamente primeiro.")

#jeito do sor
'''if ano1 < ano2:
    print('A primeira data ocorreu primeiro')
elif ano1 > ano2:
    print('A segunda data ocorreu primeiro')
else: 
    if mes1 < mes2:
        print('A primeira data ocorreu primeiro')
    elif mes1 > mes2:
        print('A segunda data ocorreu primeiro')
    else: 
        if dia1 < dia2:
            print('A primeira data ocorreu primeiro')
        elif dia1 > dia2:
            print('A segunda data ocorreu primeiro')
        else:
            print('As duas datas são iguais')'''
