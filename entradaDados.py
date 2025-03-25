nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade: '))
altura = float(input('Insira sua altura: '))
casa = int(input('Insira a quantidade de casas desejadas: '))
pi = 3.14159265359

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}")
print(f"O valor de PI com {casa} é de: {pi:.{casa}f}")
