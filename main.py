from time import sleep

# tempo_global
# tabela_eventos
# simulador

# start -> gera_1_evento

# evento -> 1 ou mais eventos e start no mais proximo
agenda = []
aleatorios = [0.1195, 0.3491, 0.9832]
eventos = [
    # Comentei esta linha, ja que o pipe faz um TypeError ao usar strings
    # {'evento': 'chX' | 'saX', 'tempo': 1, 'sorteio': 1},
]
fila = 0
tempo_global = 0


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
    agenda.append({'evento': 'ch', 'tempo': tempo + sorteio, 'sorteio': sorteio})


def agenda_saida(tempo, sorteio):
    agenda.append({'evento': 'sa', 'tempo': tempo + sorteio, 'sorteio': sorteio})


def start():
    agenda_chegada(0, 2.5)


def eventoCH(evento):
    eventos.append({'evento': 'ch', 'fila': fila, 'tempo': tempo_global})  # + tempo em cada estado da fila
    agenda_chegada()


def eventoSA(evento):
    eventos.append({'evento': 'sa', 'fila': fila, 'tempo': tempo_global})  # + tempo em cada estado da fila
    agenda_saida()


# Comentado para testar o gerador do numeros aleatorios
# while True:
#     next_evento = agenda.pop(0)
#     tempo_global = next_evento.tempo
#     if next_evento.evento == 'ch':
#         eventoCH(next_evento)
#     else:
#         eventoSA(next_evento)


# Teste do gerador de numero aleatorios
while True:
    print(quantidade_iteracoes, ' - ', congruente_linear())
    sleep(0.01)
