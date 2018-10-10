class Leitor:
    filas_lidas = []

    def __init__(self):
        with open('DEFINICOES_DE_FILAS', 'r') as input_file:
            quantidade_de_filas = input_file.readline().strip().replace('#Queue = ', '')
            quantidade_de_filas = int(quantidade_de_filas)

            for fila_atual in range(1, quantidade_de_filas + 1):
                input_file.readline()
                input_file.readline()
                nova_fila = {}
                nova_fila['probabilidades'] = []

                for fila_destino in range(1, quantidade_de_filas + 1):
                    linha = input_file.readline().strip()
                    import pdb
                    pdb.set_trace()
                    linha = linha.replace('P{0}{1} '.format(fila_atual, fila_destino), '')
                    nova_fila['probabilidades'].append(float(linha))

                linha = input_file.readline().strip()
                probabilidade_saida = linha.replace('P{0}F '.format(fila_atual, fila_destino), '')
                nova_fila['probabilidade_saida'] = float(probabilidade_saida)

                linha = input_file.readline().strip()
                probabilidade_continuar = linha.replace('P{0}C '.format(fila_atual, fila_destino), '')
                nova_fila['probabilidade_continuar'] = float(probabilidade_continuar)

                linha = input_file.readline().strip()
                servidores = linha.replace('C ', '')
                nova_fila['servidores'] = int(servidores)

                linha = input_file.readline().strip()
                capacidade = linha.replace('K ', '')
                nova_fila['capacidade']  = int(capacidade)

                linha = input_file.readline().strip()
                chegadas = linha.replace('CH ', '')
                nova_fila['chegadas'] = chegadas.split('..')

                linha = input_file.readline().strip()
                saidas = linha.replace('SA ', '')
                nova_fila['saidas'] = saidas.split('..')

                self.filas_lidas.append(nova_fila)
