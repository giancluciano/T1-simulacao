from time import sleep

# tempo_global
# tabela_eventos
# simulador

# start -> gera_1_evento

# evento -> 1 ou mais eventos e start no mais proximo
eventos = [
    # Comentei esta linha, ja que o pipe faz um TypeError ao usar strings
    {'evento': 'ch', 'tempo': 3, 'sorteio': 1},
]
fila = 0
k = 3 # tamanho da fila 

tempo_chegada = 1
tempo_saida = 2

# variaveis usadas na geracao de numeros aleatorios
x_anterior = 19
M = 4493
a = 500
c = 4
quantidade_iteracoes = 0

def get_next_evento():
    global eventos
    next_evento = eventos.pop(0)
    for evento in eventos:
        if evento['tempo'] < next_evento['tempo']:
            eventos.append(next_evento)
            next_evento = evento
            eventos.remove(evento)
    return next_evento

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


def eventoCH(evento):
    global fila
    # contabiliza 
    print('chegou ' + str(fila) + ' no tempo - ' + str(evento['tempo']))
    if fila < k:
        fila += 1
        if fila <= 1:
            agenda_saida(evento['tempo'],tempo_saida)
    agenda_chegada(evento['tempo'],tempo_chegada)


def eventoSA(evento):
    global fila
    # contabiliza
    print('saindo ' + str(fila) + ' no tempo - ' + str(evento['tempo']))
    fila -= 1
    if fila >= 1:
        agenda_saida(evento['tempo'],tempo_saida)


while True:
    next_evento = get_next_evento()
    tempo_global = next_evento['tempo']
    if next_evento['evento'] == 'ch':
        eventoCH(next_evento)
    else:
        eventoSA(next_evento)


# Teste do gerador de numero aleatorios
while True:
    print(quantidade_iteracoes, ' - ', congruente_linear())
    sleep(0.01)
