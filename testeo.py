import os
import pygame as pg
import numpy as np
from pygame.compat import geterror


# Colores
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0 ,255)
white = (255, 255, 255)
black = (0, 0, 0)
colores = [red, green, blue, white, black]
# Figure == [(point1), (point2), (point3), (point3)]
def rotate(figure, angle):
    radian = np.pi * angle / 180
    return [(round(figure[0][0] * np.cos(radian) - figure[0][1] * np.sin(radian)), round(figure[0][0] * np.sin(radian) + figure[0][1] * np.cos(radian))),
            (round(figure[1][0] * np.cos(radian) - figure[1][1] * np.sin(radian)), round(figure[1][0] * np.sin(radian) + figure[1][1] * np.cos(radian))),
            (round(figure[2][0] * np.cos(radian) - figure[2][1] * np.sin(radian)), round(figure[2][0] * np.sin(radian) + figure[2][1] * np.cos(radian))),
            (round(figure[3][0] * np.cos(radian) - figure[3][1] * np.sin(radian)), round(figure[3][0] * np.sin(radian) + figure[3][1] * np.cos(radian)))]

def figureforsurface(figure, traslacion):
    return [(figure[0][0] + traslacion, figure[0][1] + traslacion), (figure[1][0] + traslacion, figure[1][1] + traslacion),
            (figure[2][0] + traslacion, figure[2][1] + traslacion), (figure[3][0] + traslacion, figure[3][1] + traslacion)]
        
class bars():
    def __init__(self):
        barsurface = pg.Surface((200,200), pg.SRCALPHA, 32)
        pg.draw.polygon(barsurface, black, figureforsurface(basebar, 50))
        barsurface2 = pg.transform.flip(barsurface, True, False)
        barcap.blit(barsurface, (0, 700))
        barcap.blit(barsurface2, (100, 700))
        pantalla.blit(barcap, (0,0))

    def press(self): # side = left/right/both
        newcap = background.copy()
        leftbarsurface = pg.Surface((200,200), pg.SRCALPHA, 32)
        rightbarsurface = pg.Surface((200,200), pg.SRCALPHA, 32)

        leftbar = rotate(basebar, leftrotation)
        rightbar = rotate(basebar, rightrotation)

        pg.draw.polygon(leftbarsurface, black, figureforsurface(leftbar, 50))
        pg.draw.polygon(rightbarsurface, black, figureforsurface(rightbar, 50))

        newcap.blit(leftbarsurface, (25,700))
        newcap.blit(pg.transform.flip(rightbarsurface, True, False), (75, 700))

        pantalla.blit(newcap, (0,0))


#Inicio
pg.init()
leftrotation = 0
rightrotation = 0
rectangle = [(-5, 5), (45, 5), (45, -5), (-5, -5)]
basebar = rotate(rectangle, 35)
pantalla = pg.display.set_mode((300, 800))
pg.display.set_caption("Alvaro chupapico")
background = pg.Surface(pantalla.get_size())
background.fill(white)
barcap = background.copy()
clock = pg.time.Clock()
bars = bars()



#Controls

pressingleft = False
pressingright = False





# Main Loop
chuparpico = True
while chuparpico == True: 
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            chuparpico = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                pressingleft = True
            if event.key == pg.K_x:
                pressingright = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_z:
                pressingleft = False
            if event.key == pg.K_x:
                pressingright = False
        print(event)
    
    if pressingleft == True:
        if leftrotation > -70:
            leftrotation = leftrotation - 10
    if pressingright == True:
        if rightrotation > -70:
            rightrotation = rightrotation - 10
    if pressingleft == False:
        if leftrotation < 0:
            leftrotation = leftrotation + 10
    if pressingright == False:
        if rightrotation < 0:
            rightrotation = rightrotation + 10
    bars.press()

    
    pg.display.update()
