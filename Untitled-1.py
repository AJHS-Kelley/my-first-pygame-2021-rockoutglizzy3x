# pygame practice willie williams, 11/29/21 8:37, v0.0

import pygame, sys
from pygame.local import *

# start pygame 
pygame.init()

# creat game window 
windowsurfface = pygame.display._mode((500,400),0,32)
pygame.display.set_cation("hello world")

# set color values
Black = (0, 0, 0) 
White = (255, 255, 255)
Red = (255, 0, 0) 
Green = (0, 255 ,0)
Blue = (0, 0, 255)

# Set Fonts
BasicFonts = pygame.font.sysfront(None, 48)

# Setup 
text = basicFonts.render('hello world', True, White, Blue)
rextRect = text.get_rect()
textRect.centex =  windowsurfface.get_rect().centex
textRect.centery = windowsurfface.get_rect().centex

# draw a background onto widow surface.
windowsurfface.fill(White)

# draw a green polygon the surface 
pygame.draw.polygon(windowsurfface, Green, ((146, 0), (291, 106), (236,277), (56,277), (0,106)))

# draw blue line on the windowsurface
pygame.draw.polygon(windowsurfface,Blue, (60, 60), (120, 60), 4)
pygame.draw.polygon(windowsurfface,Blue, (120, 60), (60, 120))
pygame.draw.polygon(windowsurfface,Blue,  (60, 120), (120, 120),4)