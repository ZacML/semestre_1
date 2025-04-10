num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira um número inteiro: '))
num3 = int(input('Insira um número inteiro: '))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f'A ordem crescentes dos numeros digitados é: {num1} {num2} {num3}')
    else:
        print(f'A ordem crescentes dos numeros digitados é: {num1} {num3} {num2}')
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f'A ordem crescentes dos numeros digitados é: {num2} {num1} {num3}')
    else:
        print(f'A ordem crescentes dos numeros digitados é: {num2} {num3} {num1}')
elif num3 <= num1 and num3 <= num3:
    if num2 <= num1:
        print(f'A ordem crescentes dos numeros digitados é: {num3} {num2} {num1}')
    else:
        print(f'A ordem crescentes dos numeros digitados é: {num3} {num1} {num2}')