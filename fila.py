import random

class Fila:
    posicao_na_fila = 0
    capacidade_fila = 10
    perda = 0
    estados = {}
    inicio = False
    fila_saida = None
    nome = ''
    chegada = (2,4)
    saida = (2,4)
    min_chegada = chegada[0]
    max_chegada = chegada[1]
    min_saida = saida[0]
    max_saida = saida[1]
    servidores = None

    # inicio é um valor boolean que indica quando a fila recebe evento de fora
    # adicionando parametro de saida, podendo ser null ou recebendo uma outra fila
    # num futuro isso pode receber uma lista de saídas e suas porcentagens
    def __init__(self, nome, capacidade, servidores, fila_saida,chegada,saida):
        self.capacidade_fila = capacidade
        self.fila_saida = fila_saida
        self.nome = nome
        self.chegada = chegada
        self.saida = saida
        self.estados = {}
        self.servidores = servidores
        for i in range(self.capacidade_fila + 1):
            self.estados[i] = 0

    def set_inicio(self, inicio):
        self.inicio = inicio
        
    def get_saida(self):
        retorno = random.choices(range(0,len(self.fila_saida)), self.fila_saida)
        print(retorno[0])
        return retorno[0]

    def contabiliza_evento_chegada(self, evento, agenda_de_eventos, gerador):
        print('chegada na {0}, posicao_na_fila: {1} no tempo {2}'.format(self.nome,self.posicao_na_fila + 1, evento['tempo']))
        if self.posicao_na_fila < self.capacidade_fila:
            self.estados[self.posicao_na_fila] += evento['sorteio']
            self.posicao_na_fila += 1
            if self.posicao_na_fila <= self.servidores:
                sorteio = (self.max_saida - self.min_saida) * gerador.congruente_linear() + self.min_saida
                self.agenda_saida(evento['tempo'], sorteio, agenda_de_eventos)
        else:
            self.perda += 1
        sorteio = (self.max_chegada - self.min_chegada) * gerador.congruente_linear() + self.min_chegada
        self.agenda_chegada(evento['tempo'], sorteio, agenda_de_eventos)

    def contabiliza_evento_saida(self, evento, agenda_de_eventos, gerador):
        print('saindo, posicao_na_fila: {0} no tempo {1}'.format(self.posicao_na_fila + 1, evento['tempo']))
        self.estados[self.posicao_na_fila] += evento['sorteio']
        self.posicao_na_fila -= 1
        if self.posicao_na_fila >= self.servidores:
            sorteio = (self.max_saida - self.min_saida) * gerador.congruente_linear() + self.min_saida
            self.agenda_saida(evento['tempo'], sorteio, agenda_de_eventos)
            #  agenda saida para alguma lugar, tanto pra fora ou pra outra fila

    def agenda_chegada(self, tempo, sorteio, agenda_de_eventos):
        if self.inicio:
            agenda_de_eventos.append({'evento': 'ch', 'tempo': tempo + sorteio, 'sorteio': sorteio,'fila': self.nome})

    def agenda_saida(self, tempo, sorteio, agenda_de_eventos):
        agenda_de_eventos.append({'evento': 'sa', 'tempo': tempo + sorteio, 'sorteio': sorteio,'fila': self.nome})
        next_fila = self.get_saida()
        if self.fila_saida is not None and next_fila != len(self.fila_saida) - 1: # desculpa a gambi, são 2 da manha
            agenda_de_eventos.append({'evento': 'ch', 'tempo': tempo + sorteio, 'sorteio': sorteio,'fila': next_fila}) # cria uma chegada para outra fila, se tiver
