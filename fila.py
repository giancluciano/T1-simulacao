from gerador_numeros_aleatorios import Gerador

class Fila:
    posicao_na_fila = 0
    capacidade_fila = None
    perda = 0
    estados = {}

    max_chegada = 10
    min_chegada = 3
    max_saida = 8
    min_saida = 3

    gerador = Gerador()

    def __init__(self, capacidade):
        self.capacidade_fila = capacidade

        for i in range(self.capacidade_fila + 1):
            self.estados[i] = 0

    def contabiliza_evento_chegada(self, evento, eventos):
        print('chegada, posicao_na_fila:' + str(self.posicao_na_fila + 1) + ' no tempo - ' + str(evento['tempo']))
        if self.posicao_na_fila < self.capacidade_fila:
            self.estados[self.posicao_na_fila] += evento['sorteio']
            self.posicao_na_fila += 1
            if self.posicao_na_fila <= 1:
                self.agenda_saida(evento['tempo'], (self.max_saida - self.min_saida) * self.gerador.congruente_linear() + self.min_saida, eventos)
        else:
            self.perda += 1
        self.agenda_chegada(evento['tempo'], (self.max_chegada - self.min_chegada) * self.gerador.congruente_linear() + self.min_chegada, eventos)

    def contabiliza_evento_saida(self, evento, eventos):
        print('saindo, posicao_na_fila:' + str(self.posicao_na_fila + 1) + ' no tempo - ' + str(evento['tempo']))
        self.estados[self.posicao_na_fila] = self.estados[self.posicao_na_fila] + evento['sorteio']
        self.posicao_na_fila -= 1
        if self.posicao_na_fila >= 1:
            self.agenda_saida(evento['tempo'], (self.max_saida - self.min_saida) * self.gerador.congruente_linear() + self.min_saida, eventos)
            #  agenda saida para alguma lugar, tanto pra fora ou pra outra fila

    def agenda_chegada(self, tempo, sorteio, eventos):
        eventos.append({'evento': 'ch', 'tempo': tempo + sorteio, 'sorteio': sorteio})

    def agenda_saida(self, tempo, sorteio, eventos):
        eventos.append({'evento': 'sa', 'tempo': tempo + sorteio, 'sorteio': sorteio})
