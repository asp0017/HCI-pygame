import sys
import pygame
from pygame.locals import *

pygame.init()
screen_size = width, height = 1200,700 #¥þ¿Ã¹õ
screen = pygame.display.set_mode(	#¥þ¿Ã¹õ
    (width, height),
    pygame.FULLSCREEN
)
bg =  (255, 255, 255)

pygame.display.set_caption("HCI_Project")
heroPlane1 = pygame.image.load("circular-arrow_small.png")
position1 = heroPlane1.get_rect()
position1.center=(0,400)
heroPlane2 = pygame.image.load("circular-arrow_small.png")
position2 = heroPlane2.get_rect()
position2.center=(50,400)
heroPlane3 = pygame.image.load("circular-arrow_small.png")
position3 = heroPlane3.get_rect()
position3.center=(1500,400)
heroPlane4 = pygame.image.load("circular-arrow_small.png")
position4 = heroPlane4.get_rect()
position4.center=(750,800)

while True:
	for event in pygame.event.get():
		if event.type == QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
	position1 = position1.move([2.25,0])
	position2 = position2.move([2,0])
	position3 = position3.move([-2,0])
	position4 = position4.move([0,-2])
	screen.fill(bg)
	screen.blit(heroPlane1, position1)
	screen.blit(heroPlane2, position2)
	screen.blit(heroPlane3, position3)
	screen.blit(heroPlane4, position4)
	pygame.display.flip()
