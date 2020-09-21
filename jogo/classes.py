# -*- coding: UTF-8 -*-

class player:
    nome = ''
    posicao = list() # [X, Y, Z]
    vida = 0
    raio_ataque = 0 # Temporario
    forca = 0
    defesa = 0

    def __init__(self, nome):
        self.nome = str(nome)

    def ataque(self, objeto, r = None):
        dx = abs(self.posicao[0] - objeto.posicao[0])
        dy = abs(self.posicao[1] - objeto.posicao[1])
        d = (dx**2 + dy**2)**0.5
        r = r if r is not None else self.raio_ataque
        print('{} - {}'.format(d, r))
        if d <= r:
            print('Na mira, fogo!')
            objeto.vida -= self.forca
        else:
            print('Fora de alcance.')

    def vive(self):
        return False if self.vida <= 0 else True

# Area de testes
if __name__ == '__main__':
    k = list()
    for x in range(0, 2):
        k.append(player(x))
        k[x].vida = 100
        k[x].posicao = (0, 0)
        k[x].forca = 100
    del x
