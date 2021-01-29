from typing import List


class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome # Atributos da classe ficam no metodo __init__
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    germano = Pessoa(nome='Germano', idade=29)
    lourival = Pessoa(germano, nome='Lourival', idade=58)

    lourival.cnh = True # É possivel criar atributos em tempo de execução para um objeto da classe
    del germano.filhos # Remove atributos de um objeto

    print(germano.idade, lourival.filhos[0].nome)
    print(lourival.__dict__) # __dict__ contem a lista de todos os atributos o objeto