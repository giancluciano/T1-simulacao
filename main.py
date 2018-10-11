from fila import Fila
from gerador_numeros_aleatorios import Gerador
from leitor import Leitor

filas = []
leitor = Leitor()
gerador = Gerador()
capacidade_fila_1 = 10
for index, fila in enumerate(leitor.filas_lidas):
    filas.append(Fila(index,fila['capacidade'],fila['servidores'],fila['probabilidades'],fila['chegadas'],
                    fila['saidas']))
    continue
#fila2 = Fila('fila2', False, capacidade_fila_1, 1, None, (1,4), (2,8))
#fila1 = Fila('fila1', True, capacidade_fila_1, 1, fila2, (2,4), (2,5))
# parametrizado as filas que tem um inicio externo
filas[0].set_inicio(True)
iteracoes = 10000
# adicionado campo que aponta a fila qual vai receber o evento
eventos = [
    {'evento': 'ch', 'tempo': 1, 'sorteio': 1, 'fila': 0},
]


# busca o próximo evento dentro da agenda
def get_next_evento():
    global eventos
    next_evento = eventos.pop(0)
    for evento in eventos:
        if evento['tempo'] < next_evento['tempo']:
            eventos.append(next_evento)
            next_evento = evento
            eventos.remove(evento)
    return next_evento

# faz a simulação, tirando o evento da agenda e passando para a fila
iteracao_atual = 0
while True:
    if iteracao_atual >= iteracoes:
        break
    iteracao_atual += 1
    next_evento = get_next_evento()
    if next_evento['evento'] == 'ch':
        filas[next_evento['fila']].contabiliza_evento_chegada(next_evento, eventos, gerador)
    else:
        filas[next_evento['fila']].contabiliza_evento_saida(next_evento, eventos, gerador)


# Calcula o tempo percentual em cada estado


# Obtem o tempo total da simulacao
N = 0
N = get_next_evento()['tempo']

for fila in filas:
    fila.estados = { k:fila.estados[i] / N * 100 for k, i in enumerate(fila.estados)}


for fila in filas:
    {print('fila {0} estado {1}: {2:.2f}%'.format(fila.nome,i[0],i[1])) for i in fila.estados.items()}
    print('perda : {}'.format(fila.perda))
