# -*- coding: UTF-8 -*-

class entidade:
    __x = 0.0
    __y = 0.0
    __altura = 0.0
    __largura = 0.0
    __cor = '#000000'
    __sprite = None

    def setEstrutura(self, altura, largura):
        self.__altura = float(altura)
        self.__largura = float(largura)

    def setPosicao(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def setCor(self, cor):
        self.__cor = cor

    def setSprite(self, sprite):
        self.__sprite = sprite

    def getPos(self):
        return(self.__x, self.__y)

    def moveX(self, valor):
        x = self.__x + float(valor)
        self.__x = x

    def moveY(self, valor):
        y = self.__y + float(valor)
        self.__y = y

    def exibe(self):
        return self.__sprite

class player(entidade):
    nome = ''
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

class bala(entidade):
    
    

# Area de testes
if __name__ == '__main__':
    k = list()
    for x in range(0, 2):
        k.append(player(x))
        k[x].vida = 100
        k[x].posicao = (0, 0)
        k[x].forca = 100
    del x
