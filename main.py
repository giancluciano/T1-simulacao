from time import sleep

# variaveis da fila
posicao_na_fila = 0
capacidade_fila = 10


iteracoes = 10000
perda = 0
# agenda de eventos
eventos = [
    {'evento': 'ch', 'tempo': 1, 'sorteio': 1},
]

estados = {}
for i in range(capacidade_fila + 1):
    estados[i] = 0

# parametros para aleatorios
max_chegada = 10
min_chegada = 3

max_saida = 8
min_saida = 3

# variaveis usadas na geracao de numeros aleatorios
x_anterior = 19
M = 4493
a = 500
c = 4
quantidade_iteracoes = 0


def congruente_linear():
    global x_anterior, M, c, a, quantidade_iteracoes
    quantidade_iteracoes = quantidade_iteracoes + 1
    # Resto da divisao em python 3 usamos o %. Se python 2, / direto
    x_atual = (a * x_anterior + c) % M
    x_anterior = x_atual
    # Divisao no python 3 usamos /. Se python 2, precisa fazer um cast para float/Decimal
    return x_atual / M


def agenda_chegada(tempo, sorteio):
    eventos.append({'evento': 'ch', 'tempo': tempo + sorteio, 'sorteio': sorteio})


def agenda_saida(tempo, sorteio):
    eventos.append({'evento': 'sa', 'tempo': tempo + sorteio, 'sorteio': sorteio})


def start():
    agenda_chegada(0, 2.5)


#  fila
def get_next_evento():
    global eventos
    next_evento = eventos.pop(0)
    for evento in eventos:
        if evento['tempo'] < next_evento['tempo']:
            eventos.append(next_evento)
            next_evento = evento
            eventos.remove(evento)
    return next_evento


#  fila
def contabiliza_evento_chegada(evento):
    global posicao_na_fila, perda
    print('chegada, posicao_na_fila:' + str(posicao_na_fila + 1) + ' no tempo - ' + str(evento['tempo']))
    if posicao_na_fila < capacidade_fila:
        estados[posicao_na_fila] = estados[posicao_na_fila] + evento['sorteio']
        posicao_na_fila += 1
        if posicao_na_fila <= 1:
            agenda_saida(evento['tempo'], (max_saida - min_saida) * congruente_linear() + min_saida)
    else:
        perda += 1
    agenda_chegada(evento['tempo'], (max_chegada - min_chegada) * congruente_linear() + min_chegada)


#  fila
def contabiliza_evento_saida(evento):
    global posicao_na_fila
    print('saindo, posicao_na_fila:' + str(posicao_na_fila + 1) + ' no tempo - ' + str(evento['tempo']))
    estados[posicao_na_fila] = estados[posicao_na_fila] + evento['sorteio']
    posicao_na_fila -= 1
    if posicao_na_fila >= 1:
        agenda_saida(evento['tempo'], (max_saida - min_saida) * congruente_linear() + min_saida)
        #  agenda saida para alguma lugar, tanto pra fora ou pra outra fila


iteracao_atual = 0
while True:
    if iteracao_atual >= iteracoes:
        break
    iteracao_atual += 1
    next_evento = get_next_evento()
    if next_evento['evento'] == 'ch':
        contabiliza_evento_chegada(next_evento)
    else:
        contabiliza_evento_saida(next_evento)

N = 0
for i in estados.items():
    N += i[1]
for i in range(capacidade_fila + 1):
    estados[i] = estados[i] / N * 100
print(estados)

{print('{0:.2f}%'.format(i)) for i in estados.values()}
print('perda : {}'.format(perda))


# Teste do gerador de numero aleatorios
# while True:
#     print(quantidade_iteracoes, ' - ', congruente_linear())
#     sleep(0.01)
