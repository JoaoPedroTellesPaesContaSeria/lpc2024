def processar (string = str):
    string_limpa = ''
    for letra in string_limpa:
        if letra.isalnum() is True:
            string_limpa += letra
    return string_limpa.upper()


def inverter (string):
    string_inversa = ''
    for n_letra in range(len(string)):
        n_atual = len(string) - n_letra
        string_inversa += string[n_atual - 1]
    return string_inversa
        

palavra_original = input('palavra original:\n')

if processar(palavra_original) == inverter(processar(palavra_original)):
    print('é palíndromo.')
else:
    print('não é palíndromo.')