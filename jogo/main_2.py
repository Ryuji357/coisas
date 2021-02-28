# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
from PIL import Image, ImageDraw
import classes

# Personalizadas
from classes import player

def dif_tupla(t1, t2):
    return (t1[0]-t2[0], t1[1]-t2[1])

def som_tupla(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def criar_grid(img_tam, qx, qy):
    image = Image.new(mode='RGBA', size=img_tam, color=(255, 255, 255, 0))

    # objeto draw e params
    draw = ImageDraw.Draw(image)
    xy_start = 0
    y_end = image.height
    x_end = image.width

    tqx = image.width/qx
    tqy = image.width/qx

    for x in range(qx + 1):
        draw.line(
            ((tqx*x-1, xy_start), (tqx*x-1, y_end)),
            fill=(0, 0, 0),
            width=2
        )

    for y in range(qy + 1):
        '''
        draw.line(
            ((xy_start, tqy*y-1), (x_end, tqy*y-1)),
            fill=(255, 255, 255),
            width=4
        )
        '''
        draw.line(
            ((xy_start, tqy*y-1), (x_end, tqy*y-1)),
            fill=(0, 0, 0),
            width=2
        )

    del draw
    return pygame.image.fromstring(image.tobytes(), image.size, image.mode)

tamanho_tela = (640, 480)

pygame.init()
screen = pygame.display.set_mode(tamanho_tela, pygame.RESIZABLE, 32)
pygame.display.set_caption('Teste')
pygame.mouse.set_visible(False) # Desativa a figura do mouse

background = pygame.image.load('obj/teste.jpg').convert()
mouse_cursor = pygame.image.load('obj/cursor.png').convert_alpha()

grid = criar_grid(background.get_size(), 40, 30)

bg_pos = (0, 0)
dif = dif_tupla(tamanho_tela, background.get_size())
print(dif)

# Criando entidades
ents = [
    player(
        nome = 'Shazam'
    ),
]

ents[0].setSprite(pygame.image.load('obj/cursor.png').convert_alpha())

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(background, bg_pos)

        screen.blit(grid, bg_pos)

        x, y = pygame.mouse.get_pos()
        screen.blit(mouse_cursor, (x, y))

        # Resize
        if event.type == pygame.VIDEORESIZE:
            tamanho_tela = event.size
            dif = dif_tupla(tamanho_tela, background.get_size())

        # Parte que faz a imagem se mover
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_temp, y_temp = x, y
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            temp = list(som_tupla(bg_pos, dif_tupla((x, y), (x_temp, y_temp))))

            if temp[0] > 0:
                temp[0] = 0
            elif temp[0] < dif[0]:
                temp[0] = dif[0]
            if temp[1] > 0:
                temp[1] = 0
            elif temp[1] < dif[1]:
                temp[1] = dif[1]

            bg_pos = tuple(temp)
            print(bg_pos)
            x_temp, y_temp = x, y

        # Entidades
        for e in ents:
            screen.blit(e.exibe(), som_tupla(bg_pos, e.getPos()))

        pygame.display.update()

