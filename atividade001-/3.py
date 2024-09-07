def limpar(cpf):
    return cpf.replace('-', '').replace('.', '')

def validar(cpf):
    #-------etapa 1-----------
    primeiros_9 = cpf[0:9]
    lista_calc = []
    for x in range(len(primeiros_9)):
        lista_calc.append(int(primeiros_9[x]) * (10-x))

    if (sum(lista_calc) % 11) <= 2:
        if cpf[9] == '0':
            pass
        else:
            return False
    elif 11 - (sum(lista_calc) % 11) == int(cpf[9]):
        pass
    else:
        return False
    
    #-------etapa 2-----------
    primeiros_10 = cpf[0:10]
    lista_calc.clear()
    for x in range(len(primeiros_10)):
        lista_calc.append(int(primeiros_10[x]) * (11-x))

    if (sum(lista_calc) % 11) <= 2:
        if cpf[10] == '0':
            pass
        else:
            return False
    elif 11 - (sum(lista_calc) % 11) == int(cpf[10]):
        pass
    else:
        return False
    
    #se tudo tiver certo:
    return True

cpf = ''
boolcpf = False

#inserir cpf mas so funciona se digitado certo
while True:
    cpf = (input(f'validador de CPF formato XXX.XXX.XXX-XX:\n'))
    if len(cpf.replace('.', '').replace('-', '')) == 11:
        break
    else:
        print('digitou errado sei la tenta de novo')

bool_cpf = validar(limpar(cpf))

if bool_cpf is True:
    print('É válido.')
else:
    print('É inválido.')