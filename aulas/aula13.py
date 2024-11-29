# # pessoa = {
# #     'nome' : 'Aline',
# #     'sobrenome': 'Souza'
# # }

# # a, b = pessoa.values()
# # print(a,b)

# # Desempacotamento de Dicionários

# pessoa = {
#     'nome' : 'Aline',
#     'sobrenome': 'Souza'
# }

# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }

# pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)


# def mostrar_argumentos_nomeados(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'{chave} - {valor}')


# mostrar_argumentos_nomeados(**pessoas_completa)