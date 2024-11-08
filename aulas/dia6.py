# import os
# import time

# listas_compras = []

# def linha_organizar():
#     print('*' * 30)

# def listar_lista(lista):
#     if lista:
#         for i, item in enumerate(lista):
#             print(f'{i} - {item}')
#     else:
#         print('VOCÊ NÃO POSSUI NADA A SER LISTADO. TENTE NOVAMENTE...')
#     linha_organizar()

# def apagar_item_lista(lista):
#     if lista:
#         try:
#             i = int(input('QUAL O NÚMERO DO ITEM QUE VAI SER EXCLUÍDO -> '))
#             print(f'ITEM "{lista[i]}" EXCLUÍDO')
#             linha_organizar()
#             del lista[i]
#             print('Lista atualizada:', lista)
#             time.sleep(2)
#             os.system('clear')
#         except (IndexError, ValueError):
#             print("INDEX INVÁLIDO OU NÃO HÁ NADA PARA SER EXCLUÍDO")
#     else:
#         print("NÃO HÁ NADA PARA SER EXCLUÍDO")
#     linha_organizar()

# def adicionar_item(lista):
#     item_adicionado = input('QUAL ITEM VOCÊ GOSTARIA DE ADICIONAR -> ')
#     if item_adicionado:
#         lista.append(item_adicionado)
#         print('ITEM ADICIONADO COM SUCESSO!')
#         print('Lista atualizada:', lista)
#         time.sleep(2)
#         os.system('clear')
#     else:
#         print('IMPOSSÍVEL ADICIONAR UM ITEM VAZIO, TENTE NOVAMENTE...')
#     linha_organizar()

# while True:
#     linha_organizar()
#     print('LISTA DE COMPRAS DINÂMICA')
#     linha_organizar()
#     escolha_usuario = input(
#         'OLÁ, O QUE PODEMOS FAZER POR VOCÊ NA SUA LISTA? \n'
#         'DIGITE:\n[I]nserir, [D]eletar ou [L]istar -> ').lower().strip()

#     if escolha_usuario == 'i':
#         adicionar_item(listas_compras)
#     elif escolha_usuario == 'd':
#         apagar_item_lista(listas_compras)
#     elif escolha_usuario == 'l':
#         listar_lista(listas_compras)
#     else:
#         print("OPÇÃO INVÁLIDA")
#         linha_organizar()

#     sair_programa = input('DESEJA ENCERRAR O PROGRAMA? [S/N] ').lower().strip()
#     if sair_programa == 's':
#         os.system('clear')
#         time.sleep(2)
#         break

