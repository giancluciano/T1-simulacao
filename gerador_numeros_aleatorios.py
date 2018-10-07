class Gerador:
    x_anterior = 19
    M = 4493
    a = 500
    c = 4

    def congruente_linear(self):
        # Resto da divisao em python 3 usamos o %. Se python 2, / direto
        self.x_atual = (self.a * self.x_anterior + self.c) % self.M
        self.x_anterior = self.x_atual
        # Divisao no python 3 usamos /. Se python 2, precisa fazer um cast para float/Decimal
        return self.x_atual / self.M
