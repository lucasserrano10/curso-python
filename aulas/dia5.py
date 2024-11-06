# nomes = ['Lucas Serrano', 'Bárbara Barbetta', 'Arthur Lira']
# #pop()

# nomes.pop()
# print(nomes)

# #APAGA O ÚLTIMO ELEMENTO DA LISTA

# nomes.append('Arthur Lira')
# print(nomes)

# # ADICIONA ALGO NA LISTA

# del nomes[1]
# print(nomes)

# # apaga qualquer elemento da lista a partir de um indice

# # nomes.clear()
# # print(nomes)

# # nomes.append('Lucas Serrano')
# # nomes.append('Arthur Lira')
# # nomes.append('Bárbara Barbetta')
# # print(nomes)

# nomes.insert(0,'OLA')

# lista_a = [1,2,3,4]
# lista_b = [5,6,7,8,9]
# lista_a.extend(lista_b)

# print(lista_a)

# Nome = 'Luiz'
# Nome = 'Lucas'
# print(Nome)

# nomes = ['Lucas', 'João', 'Maria']
# index = 0

# for nome in nomes:
#     print(index,nome)
#     index += 1

# for i in range(0,len(nomes)):
#     for nome in nomes:
#         print(f"{i} - {nome}")


# _,nome2, *_ = ['Lucas', 'João', 'Maria']
# print(nome2)

#quando temos uma lista que não vai ser alterado nada, vamos usar as tuplas

nomes = 'Maria', 'Jonas', 'Boelt'
nomes[0] = 'BABY YOGA' # não é possivel, fazer trocas com tuplas