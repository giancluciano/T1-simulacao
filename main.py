from fila import Fila
from gerador_numeros_aleatorios import Gerador
from leitor import Leitor

leitor = Leitor()
gerador = Gerador()
capacidade_fila_1 = 10
fila2 = Fila('fila2', False, capacidade_fila_1, None, (1,4), (2,8))
fila1 = Fila('fila1', True, capacidade_fila_1, fila2, (2,4), (2,5))

iteracoes = 10000
# adicionado campo que aponta a fila qual vai receber o evento
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


# Calcula o tempo percentual em cada estado


# Obtem o tempo total da simulacao
N = 0
for i in fila1.estados.items():
    N += i[1]

for i in range(capacidade_fila_1 + 1):
    fila1.estados[i] = fila1.estados[i] / N * 100

for i in range(capacidade_fila_1 + 1):
    fila2.estados[i] = fila2.estados[i] / N * 100

{print('fila 1 estado {0}: {1:.2f}%'.format(i[0],i[1])) for i in fila1.estados.items()}
{print('fila 2  estado {0}: {1:.2f}%'.format(i[0],i[1]))for i in fila2.estados.items()}
print('perda : {}'.format(fila1.perda))
