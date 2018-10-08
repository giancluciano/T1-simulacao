class Fila:
    posicao_na_fila = 0
    capacidade_fila = None
    perda = 0
    estados = {}
    entrada = True
    saida = None

    max_chegada = 10
    min_chegada = 3
    max_saida = 8
    min_saida = 3

    # entrada é um valor boolean que indica quando a fila recebe evento de fora
    # adicionando parametro de saida, podendo ser null ou recebendo uma outra fila
    # num futuro isso pode receber uma lista de saídas e suas porcentagens
    def __init__(self, entrada, capacidade, saida):
        self.capacidade_fila = capacidade
        self.saida = saida
        self.entrada = entrada
        for i in range(self.capacidade_fila + 1):
            self.estados[i] = 0

    def contabiliza_evento_chegada(self, evento, agenda_de_eventos, gerador):
        print('chegada, posicao_na_fila: {0} no tempo {1}'.format(self.posicao_na_fila + 1, evento['tempo']))
        if self.posicao_na_fila < self.capacidade_fila:
            self.estados[self.posicao_na_fila] += evento['sorteio']
            self.posicao_na_fila += 1
            if self.posicao_na_fila <= 1:
                sorteio = (self.max_saida - self.min_saida) * gerador.congruente_linear() + self.min_saida
                self.agenda_saida(evento['tempo'], sorteio, agenda_de_eventos)
        else:
            self.perda += 1
        sorteio = (self.max_chegada - self.min_chegada) * gerador.congruente_linear() + self.min_chegada
        self.agenda_chegada(evento['tempo'], sorteio, agenda_de_eventos)

    def contabiliza_evento_saida(self, evento, agenda_de_eventos, gerador):
        print('saindo, posicao_na_fila: {0} no tempo {1}'.format(self.posicao_na_fila + 1, evento['tempo']))
        self.estados[self.posicao_na_fila] = self.estados[self.posicao_na_fila] + evento['sorteio']
        self.posicao_na_fila -= 1
        if self.posicao_na_fila >= 1:
            sorteio = (self.max_saida - self.min_saida) * gerador.congruente_linear() + self.min_saida
            self.agenda_saida(evento['tempo'], sorteio, agenda_de_eventos)
            #  agenda saida para alguma lugar, tanto pra fora ou pra outra fila

    def agenda_chegada(self, tempo, sorteio, agenda_de_eventos):
        if self.entrada:
            agenda_de_eventos.append({'evento': 'ch', 'tempo': tempo + sorteio, 'sorteio': sorteio,'fila': self})

    def agenda_saida(self, tempo, sorteio, agenda_de_eventos):
        agenda_de_eventos.append({'evento': 'sa', 'tempo': tempo + sorteio, 'sorteio': sorteio,'fila': self})
        if self.saida is not None:
            agenda_de_eventos.append({'evento': 'ch', 'tempo': tempo + sorteio, 'sorteio': sorteio,'fila': self.saida}) # cria uma chegada para outra fila, se tiver
