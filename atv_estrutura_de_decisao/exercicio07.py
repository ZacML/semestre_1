anoNasc = int(input('Ano que nasceu: '))
mesNasc = int(input('Mes que nasceu: '))
anoAtual = int(input('Ano que nasceu: '))
mesAtual = int(input('Mes que nasceu: '))

if mesNasc == mesAtual:
    print('Mês de aniversário')

idade = anoAtual - anoNasc

if mesAtual < mesNasc:
    idade = idade - 1

print("Sua idade é {idade} anos")