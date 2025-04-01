nota1 = float(input('Digite a priemira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

aulas = int (input('Insira a quantidades de aulas: '))
faltas = int(input('Insira a quantidade de faltas: '))

mediaNota = (nota1 + nota2 + nota3)/3

presenca = (aulas - faltas)

mediaPresenca = (presenca / aulas) * 100

if mediaNota >= 7 and mediaPresenca >= 75:
    print(f'Sua media é de: {mediaNota:.2f} \nSua presença é de: {mediaPresenca:.2f}% \nVocê foi APROVADO!!!')
elif mediaNota < 7 and mediaPresenca >= 75:
    print(f'Sua media é de: {mediaNota:.2f} \nSua presença é de: {mediaPresenca:.2f}% \nVocê esta em RECUPERAÇÃO!!!')
else:
    print(f'Sua media é de: {mediaNota:.2f} \nSua presença é de: {mediaPresenca:.2f}% \nVocê foi REPROVADO!!!')
