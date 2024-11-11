# cpf_usuario = input('DIGITE SEU CPF (APENAS NÚMEROS) *vamos valida-lo ->')
# nove_digitos = cpf_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito_1 in nove_digitos:
#     resultado_digito_1 += int(digito_1) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
#     digito_2 = resultado_digito_2 *10 %11


# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_usuario}, CPF VÁLIDO')
# else:
#     print('CPF INVÁLIDO')


# CRIANDO UM GERADOR DE CPF

