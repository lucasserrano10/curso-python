def verificar_operacao():
    operacoes = ['duplicar','triplicar','quadruplicar']
    operacao = input('OQUE DESEJA FAZER [DUPLICAR,TRIPLICAR,QUADRUPLICAR] -> ').lower().strip()
    if operacao not in operacoes:
        print('DIGITE UMA OPERAÇÃO VÁLIDA')
    return operacao



def multiplicar_duplicar(num,operacao):
    if operacao == 'duplicar':
        return num * 2
    elif operacao == 'triplicar':
        return num * 3
    elif operacao == 'quadruplicar':
        return num * 4
    else:
        print('OPERAÇÃO INVÁLIDA')
    

num = input('DIGITE UM NÚMERO VÁLIDO -> ')
num = int(num)
operacao = verificar_operacao()
resultado = multiplicar_duplicar(num,operacao)
print(resultado)

    