# tempo_global
# tabela_eventos
# simulador

# start -> gera_1_evento

# evento -> 1 ou mais eventos e start no mais proximo
agenda = []
aleatorios = [0.1195, 0.3491, 0.9832]
eventos = [
            {'evento': 'chX' | 'saX', 'tempo': 1, 'sorteio': 1},
          ]
fila = 0
tempo_global = 0


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


while True:
    next_evento = agenda.pop(0)
    tempo_global = next_evento.tempo
    if next_evento.evento == 'ch':
        eventoCH(next_evento)
    else:
        eventoSA(next_evento)
