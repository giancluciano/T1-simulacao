from fila import Fila
from gerador_numeros_aleatorios import Gerador

gerador = Gerador()
capacidade_fila_1 = 10
fila2 = Fila(False, capacidade_fila_1, None)
fila1 = Fila(True, capacidade_fila_1, fila2)

iteracoes = 10000
# adcionado campo que aponta a fila qual vai receber o evento
eventos = [
    {'evento': 'ch', 'tempo': 1, 'sorteio': 1, 'fila': fila1},
]


def get_next_evento():
    global eventos
    next_evento = eventos.pop(0)
    for evento in eventos:
        if evento['tempo'] < next_evento['tempo']:
            eventos.append(next_evento)
            next_evento = evento
            eventos.remove(evento)
    return next_evento

iteracao_atual = 0
while True:
    if iteracao_atual >= iteracoes:
        break
    iteracao_atual += 1
    next_evento = get_next_evento()
    if next_evento['evento'] == 'ch':
        next_evento['fila'].contabiliza_evento_chegada(next_evento, eventos, gerador)
    else:
        next_evento['fila'].contabiliza_evento_saida(next_evento, eventos, gerador)

# Obtem o tempo total da simulacao
N = 0
for i in fila1.estados.items():
    N += i[1]

# Calcula o tempo percentual em cada estado
for i in range(capacidade_fila_1 + 1):
    fila1.estados[i] = fila1.estados[i] / N * 100
print(fila1.estados)

{print('{0:.2f}%'.format(i)) for i in fila1.estados.values()}
{print('{0:.2f}%'.format(i)) for i in fila2.estados.values()}
print('perda : {}'.format(fila1.perda))
