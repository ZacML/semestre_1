nm = str(input('Insira seu nome: '))
sexo = str(input('Insira seu sexo: '))
peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
imc = float(peso / (altura*2))

#nm = 'Jorge'
#sexo = 'Masculino'
#peso = 83.5
#altura = 1.83
#imc = peso / (altura*2)

if sexo == "masculino":
     print(f"Senhor {nm} seu IMC é: {imc:.2f}")

elif sexo == "feminino":
    print(f"Senhora {nm} seu IMC é: {imc:.2f}")
