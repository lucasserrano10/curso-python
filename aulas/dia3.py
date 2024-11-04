# velocidade = 61
# local_carro = 90

# RADAR_1 = 60
# LOCAL_1 = 100 # como se fosse um CONST em javascript
# RADAR_RANGE = 1

# if velocidade > RADAR_1:
#     print('VELOCIDADE CARRO PASSOU DO RADAR 1')

# if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
#     print('CARRO MULTADO NO RADAR 1')

# num_usuario = int(input('DIGITE UM NÚMERO INTEIRO ->'))
# if num_usuario % 2 == 0:
#     print(f'O NÚMERO DIGITADO {num_usuario} É PAR')
# else:
#     print('O NÚMERO É IMPAR')


# hora_usuario = int(input('DIGITE O HORÁRIO -->'))
# if hora_usuario >= 6 and hora_usuario <= 12:
#     print('BOM DIA')
# elif hora_usuario >= 13 and hora_usuario <= 18:
#     print('BOA TARDE')
# else:
#     print('BOA NOITE')

# i = 0
# while True:
#     i+=1
#     print(i)
#     if i >= 10:
#         break
# print('ACABOUUUU !')

# continue volta para o loop

# contador = 0

# while contador <= 15:
#     contador += 1

#     if contador == 6:
#         print('Não vou mostrar o 6')
#         continue

#     if contador >= 10 and contador <= 15:
#         print('NÃO VOU MOSTRAR O CONTADOR', contador)
#         continue

#     print(contador)

#     if contador == 12:
#         break

nome = 'Lucas Serrano'
index_nome = len(nome) - 1
i = 0
while i <= index_nome:
    print(nome[i])
    i += 1