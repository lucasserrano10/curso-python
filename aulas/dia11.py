# s1 = {'Luiz', 1,2,3}
# print(s1)

# s1 = set()
# print(s1)

# s1 = {1,2,3,3,3,3,3,4}
# print(s1)
# s1 = list(s1)
# print(s1[0])

# Métodos úteis:
# Add, Update, Clear, Discard

# s1 = set()
# s1.add('Lucas')
# s1.add(18)
# print(s1)
# s1.update('Serrano')
# print(s1)
# # s1.clear()
# # print(s1)
# s1.discard(18)

# Operadores úteis:
# União (union) |
# Interseção &
# Diferença -
#  Diferença simétrica ^ itens que não estao em ambosw
# s1 = {1,2,3,4}
# s2 = {4,5,6}
# s3 = s1 | s2 # uniao
# s3 = s1 & s2 # intersecao
# s3 = s1 - s2 # diferenca
# s3 = s1 ^ s2 # diferenca simetrica
# print(s3)

# EXEMPLO DE USO
# letras = set()
# while True:
#     letra = input('Digite:')
#     letras.add(letra)

#     if 'l' in letras:
#         print('Parabéns')
#         break

#     print(letras)

lista_de_listas_inteiros = [
    [1, 2, 4, 6, 7, 8, 9, 4, 3, 1, 5, 3],
    [1,2,3,4,5,6,7,8,9],
    [1, 2, 4, 3, 7, 8, 9, 4, 3, 1, 5, 3],
    [1, 2, 4, 6, 2, 8, 9, 4, 3, 9, 5, 3],
    [1, 2, 4, 6, 7, 4, 4, 4, 3, 1, 5, 3],
]

for i, lista in enumerate(lista_de_listas_inteiros):
    print(i, lista)
    
    lista_sem_duplicados = set(lista)  
    if len(lista_sem_duplicados) == len(lista): 
        print(-1)
    else:
        qtdade_duplicados = len(lista) - len(lista_sem_duplicados)
        print(f'OCORREU {qtdade_duplicados} VEZES A DUPLICAÇÃO DE NÚMEROS')
