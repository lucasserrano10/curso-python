# import os
# import time


# a = 5
# b = 5
# def soma(a,b):
#     resultado =  a + b
#     return resultado

# print(f'A SOMA DE A + B É {soma(a,b)}')



# time.sleep(4)
# os.system("clear")

# def soma(*args):
#     total = 1
#     for n in args:
#         total *= n
#     return total


# soma_valores = soma(1,2,3,4,5,7)
# print(soma_valores)


# def par_impar(a):
#     if a % 2 == 0:
#         return f'{a} é par'
#     return f'{a} é impar'

# verificar_numero = par_impar(346)

# print(verificar_numero)

# HIGH ORDER FUNCTIONS

# def funcao(msg):
#     return msg

# def executa_function(funcao):
#     return function()

# CLOSURE

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('BOM DIA', 'LUIZ')
s2 = criar_saudacao('BOA NOITE', 'LUIZ')

print(s1())