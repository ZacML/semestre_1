ladoA = float(input('Insira o lado "A" do triangulo ').strip)
ladoB = float(input('Insira o lado "B" do triangulo ').strip)
ladoC = float(input('Insira o lado "C" do triangulo ').strip)

if (ladoA + ladoB) > ladoC and (ladoA + ladoC) > ladoB and (ladoB + ladoC) > ladoA:
    if (ladoA == ladoB and ladoA ==ladoC):
        print('O triangulo é equilatéro')
    elif (ladoA == ladoB or ladoA == ladoC):
        print('O triangulo é Isósceles')
    else:
     print('O triangulo é escaleno')
else:
   print('Não é possivel criar um triangulo com os números inseridos')
