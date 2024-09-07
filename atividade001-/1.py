from random import randrange

n_dado = 6
n_rolagens = 100
total_por_n = []

def rolar(lados, rolagens):

    #lista local
    l_resultado = []

    for x in range(rolagens):
        l_resultado.append(randrange(1, lados + 1))

    return l_resultado

for x in range(n_dado):
    total_por_n.append(0)

for resultado_individual in rolar(n_dado, n_rolagens):
    n = resultado_individual - 1
    total_por_n[n] = total_por_n[n] + 1

for n in range(len(total_por_n)):
    print(f'total de vezes que deu {n+1}: {total_por_n[n]} ({(total_por_n[n]/n_rolagens * 100):.2f}%)')