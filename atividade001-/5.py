import os
import random

path = 'palavras.txt'
with open(path, 'r') as arquivo_txt:
    conteudo = arquivo_txt.read()
lista_respostas = conteudo.split('\n')

#selecionar palavra aleatória da lista de possibilidades
def selecionar_palavra():
    return lista_respostas[random.randrange(len(lista_respostas))]

#função principal do jogo com entrada para resposta e quantidade de erros aceita
def jogar (resposta = str, 
           chances = int):
    
    #preparação inicial
    resposta = resposta.upper()
    forca = []
    letras_usadas = []
    display = '\n\n\n'

    for letra in resposta:
        if letra.isalnum() is True and letra != '_':
            forca.append([letra, False])
        else:
            forca.append([letra, True])

    #-----loop de gameplay-----
    while chances > 0:
        #impressão do boneco
        if chances == 1:
            boneco = ('_________\n'
                      + '|        |\n'
                      + '|        O\n'
                      + '|       [|]\n'
                      + '|       ( \n'
                      + '|\n'
                      + '|  ')
        elif chances == 2:
            boneco = ('_________\n'
                      + '|        |\n'
                      + '|        O\n'
                      + '|       [|]\n'
                      + '|        \n'
                      + '|\n'
                      + '|  ')
        elif chances == 3:
            boneco = ('_________\n'
                      + '|        |\n'
                      + '|        O\n'
                      + '|       [|\n'
                      + '|\n'
                      + '|\n'
                      + '|  ')
        elif chances == 4:
            boneco = ('_________\n'
                      + '|        |\n'
                      + '|        O\n'
                      + '|        |\n'
                      + '|\n'
                      + '|\n'
                      + '|  ')
        elif chances == 5:
            boneco = ('_________\n'
                      + '|        |\n'
                      + '|        O\n'
                      + '|\n'
                      + '|\n'
                      + '|\n'
                      + '|  ')
        elif chances >= 6:
            boneco = ('_________\n'
                      + '|        |\n'
                      + '|\n'
                      + '|\n'
                      + '|\n'
                      + '|\n'
                      + '|  ')
            
        #impressão do hud principal
        display += boneco
        for letra in forca:
            if letra[1] == True:
                display += letra[0] + ' '
            else:
                display += '_ '
        display += f'\nerros restantes: {chances}.\n'
        if len(letras_usadas) > 0:
            display += 'letras já usadas: [ '
            for x in letras_usadas:
                display += x + ' '
            display += ']\n'
        
        print(display)
        display = '\n\n\n\n\n\n'


        #leitura e análise de tentativas entradas
        tentativa = 'placeholder'
        while True:
            tentativa = input('Insira uma letra: ').upper()
            if len(tentativa) == 1:
                usada = False
                for letra in letras_usadas:
                    if tentativa == letra:
                        usada = True
                        print('use uma letra nova.')
                if usada == False:
                    print(letra, letras_usadas)
                    break
        
        #verificação se a tentativa foi correta ou incorreta
        correto = False
        for letra in forca:
            if letra[0] == tentativa:
                letra[1] = True
                correto = True
        if correto is False:
            chances -= 1
        letras_usadas.append(tentativa)

        vitoria = True
        for letra in forca:
            if letra[1] == False:
                vitoria = False
        
        #fim de jogo caso condição de vitória seja alcançada antes do fim do loop
        if vitoria == True:
            print('\n\n\n\n\n\n\n\n\n' + boneco + resposta + '\nParabéns, venceu.')
            return None
    #fim do jogo caso a condição de vitória não seja alcançada e o loop termine.
    boneco = ('_________\n'
              + '|        |\n'
              + '|        O\n'
              + '|       [|]\n'
              + '|       ( )\n'
              + '|\n'
              + '|  ')
    print('\n\n\n\n\n\n\n\n' + boneco + 'Perdeu mané a resposta era ' + resposta)
    return None

#call da função principal
jogar(selecionar_palavra(), 6)