lista_n1 = ['vinte', 'trinta', 'quarenta', 'cinquenta',
            'sessenta', 'setenta', 'oitenta', 'noventa']
lista_n2 = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

lista_dez = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

def extensificar (n_inteiro = int):
    n_extenso = ''
    n_string = str(n_inteiro)

    if len(n_string) == 1:
        return lista_n2[n_inteiro]
    else:
        n_1 = int(n_string[0])
        n_2 = int(n_string[1])

        if n_1 >= 2:
            n_extenso += lista_n1[n_1 - 2]

            if n_2 != 0:
                n_extenso += (' e ' + lista_n2[n_2])
        if n_1 == 1:
            n_extenso = lista_dez[n_2]

    return n_extenso


while True:
    numero_entrada = input('extensificador de número de 0 a 99\nnúmero: ')
    try:
        int(numero_entrada)
    except:
        print('apenas números.')
    else:
        break

print(extensificar(numero_entrada))