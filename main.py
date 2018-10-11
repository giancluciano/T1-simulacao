from fila import Fila
from gerador_numeros_aleatorios import Gerador
from leitor import Leitor

filas = []
leitor = Leitor()
gerador = Gerador()
for index, fila in enumerate(leitor.filas_lidas):
    filas.append(
        Fila(index, fila['capacidade'], fila['servidores'], fila['probabilidades'], fila['chegadas'], fila['saidas'])
    )

# Considera apenas a fila 1 como recebendo entradas externas
filas[0].set_inicio(True)
iteracoes = 10000
eventos = [
    {'evento': 'ch', 'tempo': 1, 'sorteio': 1, 'fila': 0}  # 0 corresponde a fila 1,
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
    fila = filas[next_evento['fila']]
    if next_evento['evento'] == 'ch':
        fila.contabiliza_evento_chegada(next_evento, eventos, gerador)
    else:
        fila.contabiliza_evento_saida(next_evento, eventos, gerador)

# Obtem o tempo total da simulacao
N = 0
N = get_next_evento()['tempo']

# Calcula o tempo percentual em cada estado
for fila in filas:
    fila.estados = { k:fila.estados[i] / N * 100 for k, i in enumerate(fila.estados)}

# Apresenta os resultados
for fila in filas:
    {print('fila {0} estado {1}: {2:.2f}%'.format(fila.nome,i[0],i[1])) for i in fila.estados.items()}
    print('perda : {}'.format(fila.perda))
