#   List Conprehension em Python
# Forma rápida e criar listas

# print(list(range(10)))

# lista = []
# for num in range(10):
#     lista.append(num)
# print(lista)

# lista = [numero for numero in range(10)]
# print(lista)
# lista = [numero * 2 for numero in range(10)]
# print(lista)

# produtos = [
#     {'nome': 'p1', 'preco' : 10},
#     {'nome': 'p2', 'preco' : 40},
#     {'nome': 'p3', 'preco' : 50},
# ]

# novos_produtos = [{'nome' :produto['nome'], 'preco': produto['preco'] * 0.9} for produto in produtos]
# print(novos_produtos)

# # Um list comprehension para diminuir 10% na black friday

# esquerda do for é mapeamento, a direita é filto


produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 40},
    {'nome': 'p3', 'preco': 50},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

print(novos_produtos)
