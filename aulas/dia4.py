# # calculadora com while
# import time

# def linha_organizada():
#     print(f'*'*30)
#     return

# print('BEM VINDO A CALCULADORA !')
# linha_organizada()
# while True:
#     valor_1 = input('DIGITE O PRIMEIRO VALOR ->')
#     valor_2 = input('DIGITE O SEGUNDO VALOR ->')
#     operador = input('DIGITE O OPERADOR [+, -, /, *] ->')

#     numero_validos = None

#     try:
#         valor_1_verificado = float(valor_1)
#         valor_2_verificado = float(valor_2)
#         numero_validos = True
#     except:
#         numero_validos = None

#     if numero_validos == None:
#         print('UM OU AMBOS OS NÚMEROS DIGITADOS SÃO INVÁLIDOS')
#         continue

#     operadores_permitidos = '+-/*'

#     if operador not in operadores_permitidos:
#         print('Operador inválido')
#         continue

#     if len(operador) > 1:
#         print('DIGITE APENAS UM OPERADOR !')
#         continue

#     if operador == '+':
#         print('Realizando sua operação...')
#         time.sleep(2)
#         linha_organizada()
#         print(f'{valor_1_verificado} + {valor_2_verificado} = {valor_1_verificado+valor_2_verificado}')
#         linha_organizada()
#     elif operador == '-':
#         print('Realizando sua operação...')
#         time.sleep(2)
#         linha_organizada()
#         print(f'{valor_1_verificado} - {valor_2_verificado} = {valor_1_verificado-valor_2_verificado}')
#         linha_organizada()
#     elif operador == '*':
#         print('Realizando sua operação...')
#         time.sleep(2)
#         linha_organizada()        
#         print(f'{valor_1_verificado} x {valor_2_verificado} = {valor_1_verificado*valor_2_verificado}')
#         linha_organizada()
#     elif operador == '/':
#         print('Realizando sua operação...')
#         time.sleep(2)
#         linha_organizada()
#         print(f'{valor_1_verificado} + {valor_2_verificado} = {valor_1_verificado+valor_2_verificado}')
#         linha_organizada()

#     sair = input('DESEJA SAIR DO AMBIENTE [SIM/NÃO] ->').lower().strip()
#     if sair != 'não':
#         break

# frase = 'O Python é uma linguagem de programação multiparadigma'

# usuario_count = input('QUAL LETRA OU FRASE QUER SABER QUANTAS VEZES PASSA PELA FRASE -->').lower().strip()

# i = 0
# qtdade = 0
# while i < len(frase):
#     letra_atual = frase[i]
#     if letra_atual == usuario_count:
#         qtdade += 1
#     i+=1

# print(f'FOI ENCONTRADO A LETRA {usuario_count}, {qtdade} VEZES')


# for i in range(1,6):
#     for j in range(1,4):
#         print(f'LINHA{i}, COLUNA{j}')


#DESAFIO 1
# deixe uma palavra secreta
#a medida que a pessoa colocar uma letra, conte as tentativas
#deixe astericos e a medida que ela for acertando as letras troque o asteriscos pela letra que forma a palavra
# quando a pessoa acertar coloque que ela ganhou, a palabvra e quantas tentativas foram necessarias
# se ela não digitar nada obrigue ela digitar algo
# se ela digitar algo maior que uma letra, fale que esta inválido

import os

palavra_secreta = 'SORVETE'
letras_acertadas = ''
tentativas = 0

while True:
    letra_usuario = input('DIGITE UMA LETRA ->')
    tentativas += 1
    if len(letra_usuario) > 1 or len(letra_usuario) == 0:
        print('DIGITE UMA LETRA VÁLIDA !')
        continue
    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palavra_formada = ''    

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU !!!')
        print(f'A PALAVRA ERA {palavra_formada}')
        print(f'VOCÊ USOU {tentativas} TENTATIVAS')
        letras_acertadas = ''
        tentativas = 0