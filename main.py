import textos as txt
import os

print('Salve, salve caro usuário? Bem-vindo ao PROJETO TABELANBA.')
while True:
    print('O que deseja fazer hoje? Digite NBA para ler sobre NBA ou TBNA para ler sobre o projet e SAIR para sair do programa.')
    verificar = str(input('Digite sua opção: '))
    while verificar != "NBA" and verificar != "TNBA" and verificar != "SAIR":
        verificar = str(input('Digite uma opção válida: '))
    else:
        os.system('cls')
    if verificar == "NBA":
        os.system('cls')
        print(txt.sobreNBA)
    elif verificar == "TNBA":
        os.system('cls')
        print(txt.sobreTABELANBA)
    else:
        break