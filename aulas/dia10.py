# carros = [
#     {'marca' : 'BMW', 'motor' : '500cv'},
#     {'marca' : 'AUDI', 'motor' : '300cv'},
#     {'marca' : 'PORSCHE', 'motor' : '780cv'},
#     {'marca' : 'FERRARI', 'motor' : '1000cv'},
# ]

# for carro in carros:
#     for chave,valor in carro.items():
#         print(f'{chave} - {valor} \n')

# pessoas = {
#     'nome' : 'Lucas',
#     'job' : 'programmer',
#     'age' : 32,
#     'endereço': [
#         {'rua': 'tal tal', 'número' : 123},
#         {'rua': 'tal tal', 'número' : 321},
#     ]
# }

# print(pessoas['endereço'][1])

# for chave in pessoas:
#     print(chave, pessoas[chave])

# pessoas['nome'] = 'Arthur'
# print(pessoas)

# if pessoas.get('nome'):
#     print('Chave Existente')
# else:
#     print('Chave não existe !')

# pessoas = {
#     'nome' : 'Lucas',
#     'job' : 'programmer',
#     'age' : 32,
# }

# print(len(pessoas))
# print(list(pessoas.keys()))
# print(list(pessoas.values()))

# for chave, valor in pessoas.items():
#     print(chave, valor)

# pessoas.setdefault('altura', 0)
# print(pessoas)

# d1 = {
#     'c1' : 1,
#     'c2' : 2,
#     # 'c3' : [1,2,3] esse aqui se trocassemos a lista trocaria das duas listas, pois é apenas cópia rasa
# }

# d2 = d1.copy() # cópia rasa, porém se tiver um lista ou muitos níveis, ele nao vai funcionar direito, apenas copias rasas e mutáveis

# d2['c1'] = 1000
# print(d1)
# print(d2)

# # para fazer um cópia profunda temos que importar copy e usar o deepcopy

# p1 = {
#     'nome' : 'Lucas',
#     'sobrenome' : 'Serrano'
# }

# print(p1.get('sobrenome', 'Não Existe'))

# p1.pop('nome')
# print(p1)

# p1.update({
#     'nome' : 'Novo Valor',
#     'idade' : 19,
# })

# print(p1)

perguntas = [
    {
        'Pergunta' : 'Quanto é 2*2?',
        'Opções' : ['1', '4', '3', '2'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 2+3?',
        'Opções' : ['5', '4', '6', '2'],
        'Resposta' : '5',
    },
    {
        'Pergunta' : 'Quanto é 2*10?',
        'Opções' : ['18', '10', '200', '20'],
        'Resposta' : '20',
    },
]

print()
print('----BEM VINDO AO QUIZ----')
print()
score = 0
index = 0
while index < len(perguntas):
    print(perguntas[index]['Pergunta'])
    print()
    print('Opções :')
    indices = 0
    for valor in perguntas[index]['Opções']:
        print(f'{indices}) {valor}')
        indices += 1
    opcao = int(input('Escolha uma opção :'))
    if opcao < 0 or opcao >= len(perguntas[index]['Opções']):
        print("Escolha uma opção válida entre os índices disponíveis.")
        continue
    if perguntas[index]['Opções'][opcao] == perguntas[index]['Resposta']:
        print('Você Acertou ✅')
        print()
        score += 1
        index += 1
    else:
        print('Você Errou 🚨')
        print()
        index += 1
print(f'Você Acertou {score} de 3 !')

