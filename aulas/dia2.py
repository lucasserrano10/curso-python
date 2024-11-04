# a = 'A'
# b = 'B'
# c = 1.1
# formato = 'a={}'.format(a, b ,c)
# print(formato)

# print(f'lucas doido é {c}')
# pergunta_nome = input('DIGITE SEU NOME -> ')
# print(f'NOME DO USUÁRIO : {pergunta_nome}')

# pergunta_saida = input('DESEJA ENTRAR NO PORTAL OU SAIR -->').lower()
# if pergunta_saida != 'entrar':
#     print('CERTO, SAINDO DO SISTEMA...')
# else:
#     print('ENTRANDO NO SISTEMA...')


# def valores_recursivos():
#     primeiro_valor = input('DIGITE O PRIMEIRO VALOR ->')
#     segundo_valor = input('DIGITE O SEGUNDO VALOR ->')
#     if primeiro_valor > segundo_valor:
#         print(f'O PRIMEIRO VALOR {primeiro_valor} É MAIOR QUE O SEGUNDO VALOR {segundo_valor}')
#     elif segundo_valor > primeiro_valor:
#         print(f'O SEGUNDO VALOR {segundo_valor} É MAIOR QUE O PRIMEIRO VALOR {primeiro_valor}')
#     elif primeiro_valor == segundo_valor:
#         print('AMBOS NÚMEROS TEM O MESMO VALOR')
#         pergunta_repetir = input('GOSTARIA DE TENTAR NOVAMENTE [sim/não]').lower()
#         if pergunta_repetir == 'sim':
#             valores_recursivos()434
#         else:
#             print(f'*'*30)
#             print('ENCERRANDO O SISTEMA...')
# valores_recursivos()


# senha = '123456'

# pergunta_usuario = input('DIGITE A SENHA ->')

# if not pergunta_usuario:
#     print('NÃO DIGITOU NADA !')

# if senha == '123456':
#     print('senha CORRETA')
# else:
#     print('CORRETstr

# string = 'mundo'
# copiaString = string[:]
# print(copiaString[:2])
# len_de_string = len(string) - 1
# print(string[len_de_string])

# nome = ' Lucas Serrano'
# print(nome[::-1])

try:
    print('TESTANDO TRATAMENTO DE ERROS')
    int('a')
except:
    print('Não é Possível transformar String em número')